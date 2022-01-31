from django.db import models
from django.db.models.query_utils import PathInfo
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, F, Func, Value, CharField
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView
from django.db import transaction

import json
import math
# import json_tricks

from django.core.serializers.json import DjangoJSONEncoder
# from django.core.serializers import serialize

from .con_models import ContactModel,AlternateEmailModel,AlternatePhoneModel,PersonalAddressModel,TestCheckboxModel,GendersModel
from .con_contact_form_control import CheckFormCreateContact
from .con_alternate_e_form_control import CheckFormCreateAlternateEmail
from .con_alternate_p_form_control import CheckFormCreateAlternatePhone
from .con_personal_a_form_control import CheckFormCreatePersonalAddress

# Create your views here.

class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        stand_of_create_contact = CheckFormCreateContact(None)
        stand_of_create_alternate_email = CheckFormCreateAlternateEmail(None)
        stand_of_crate_alternate_phone = CheckFormCreateAlternatePhone(None)
        stand_of_crate_personal_address = CheckFormCreatePersonalAddress(None)
        call_testchk_queryset = TestCheckboxModel.objects.select_related('chk_gender').values('chk_id','chk_name').annotate(
             gender_id=F("chk_gender"), gender_title=F("chk_gender__genders_title")
        )

        new_obj = {}
        new_gender_list = []
        gender_value = []
        final_obj_list = []
        update_obj = {}
        sub_obj = {
            "gender_id": None,
            "gender_title": None,
        }

        for item in call_testchk_queryset:
            get_chk_id = item["chk_id"]
            print("item = {} ".format(item))
            if new_obj and ("chk_id" in new_obj) and (new_obj["chk_id"] == get_chk_id):
                update_obj = { "gender_id": item["gender_id"],"gender_title": item["gender_title"]}
                new_gender_list.append(sub_obj.update(update_obj))
                # print("gender_list = ", new_gender_list)
                gender_value = new_gender_list
                # print("gender_value = ", gender_value)
                # print("new_obj = ", new_obj)
                for item in final_obj_list:
                    if item["chk_id"] == new_obj["chk_id"]:
                        for v in gender_value:
                            item["chk_gender"].append(v)
                        print("item in fianl = ", item)
                        break
                new_gender_list.clear()
            else:
                update_obj = { "gender_id": item["gender_id"],"gender_title": item["gender_title"]}
                print("update_obj = {} --> type = {} ".format(update_obj,type(update_obj)))
                new_gender_list.append(sub_obj.update(update_obj))
                # print("gender_list = ", new_gender_list)
                new_obj = item.copy()
                gender_value = new_gender_list
                # print("gender_value = ", gender_value)
                edit_obj = {"chk_gender": list(gender_value)}
                new_obj.update(edit_obj)
                # print("new_obj = ", new_obj)
                final_obj_list.append(dict(new_obj))
                new_gender_list.clear()

        print("final_obj_list = {} --> type = {} \n".format(final_obj_list, type(final_obj_list)))

        for item in final_obj_list:
            print("item = {} --> type = {} ".format(item, type(item)))

        base_context = {
            'web_title': 'Contact (Index Page)',
            'form_contact': stand_of_create_contact,
            'form_alternate_email': stand_of_create_alternate_email,
            'form_alternate_phone': stand_of_crate_alternate_phone,
            'form_personal_address': stand_of_crate_personal_address
        }
        return render(request, 'con_index.html', base_context)

class ShowMainDataView(ListView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('page') or (request.GET.get('search_by') and request.GET.get('value')):
            set_maxbase_page = 3
            base_limit_record = 5
            try:
                base_page = int(request.GET.get('page'))
                get_key_search = (None if request.GET.get('search_by') == "undefined" else request.GET.get('search_by'))
                get_value_search = (None if request.GET.get('value') ==  "undefined" else request.GET.get('value'))
                print('get_obj_request = ', get_key_search, '-->', type(get_key_search))
                print('get_value_search = ', get_value_search, '-->', type(get_value_search))
                print('base_page =', base_page)
                if get_key_search and get_value_search:

                    def GetQuseryObjByKey(key_search, value_search):
                            if key_search == 'hn':
                                print('come to hn')
                                get_obj_from_query = ContactModel.objects.select_related('gender').filter(Q(hn__icontains=value_search)).values(
                                'pk','hn','f_name_th','l_name_th','mobile_phone','gender','nationality','email','date_of_birth').annotate(
                                gender_title=F("gender__genders_title"), nationality_title=F("nationality__nationality_title")
                                ).order_by("time_created")
                                return get_obj_from_query
                            elif key_search == 'gender':
                                print('come to gender')
                                get_obj_from_query = ContactModel.objects.select_related('gender').filter(Q(gender__genders_title__istartswith=value_search) | Q(gender__genders_title__iendswith=value_search)).values(
                                'pk','hn','f_name_th','l_name_th','mobile_phone','gender','nationality','email','date_of_birth').annotate(
                                gender_title=F("gender__genders_title"), nationality_title=F("nationality__nationality_title")
                                ).order_by("time_created")
                                return get_obj_from_query

                    get_all_queryset = GetQuseryObjByKey(get_key_search, get_value_search)   #final_obj_from_search
                    get_total_queryset = get_all_queryset.count()

                else:
                    get_all_queryset = ContactModel.objects.values('pk','hn','f_name_th','l_name_th','mobile_phone','gender','nationality','email','date_of_birth').annotate(
                        gender_title=F("gender__genders_title"), nationality_title=F("nationality__nationality_title")
                    ).order_by("time_created")
                    get_total_queryset = get_all_queryset.count()

                def cal_paginators(end_contact, start_contact, total_records, base_max_page):
                    pervious_status = False
                    next_status = False

                    min_record = ((start_contact-1) * end_contact)  #+1
                    max_record = (start_contact * end_contact)

                    predict_max_page = math.ceil(total_records/end_contact)
                    n = int((start_contact-1)/base_max_page) + 1
                    min_page = base_max_page * (n - 1) + 1
                    max_page = base_max_page * n

                    print(end_contact)
                    print('n = ', n)
                    print('min_record = ', min_record)
                    print('max_record = ', max_record)
                    print('predict_max_page = ', predict_max_page)
                    print('min_page = ', int(min_page))
                    print('max_page = ', int(max_page))

                    if max_page > predict_max_page:
                        max_page = predict_max_page
                    else:
                        next_status = True

                    if n > 1:
                        pervious_status = True

                    dict_paginate = {
                        'min_record': min_record,
                        'max_record': max_record,
                        'min_page': int(min_page),
                        'max_page': int(max_page),
                        'mes': {
                            'pervious': pervious_status,
                            'next': next_status,
                        }
                    }
                    return dict_paginate

                get_cal_stant = cal_paginators(base_limit_record, base_page, get_total_queryset, set_maxbase_page)
                print('get_cal_stant  =', get_cal_stant, '-->', type(get_cal_stant))
                final_queryset = get_all_queryset[get_cal_stant['min_record']:get_cal_stant['max_record']]
                print(final_queryset)
                context = {
                    'data': {
                        'data_contact_list': list(final_queryset),
                        'data_total_contact': get_total_queryset,
                        'data_minpage': get_cal_stant['min_page'],
                        'data_maxpage': get_cal_stant['max_page'],
                        'mes': get_cal_stant['mes'],
                    }
                }
                return JsonResponse(context)
            except Exception as e:
                print('queryset Error =', e);
                context = {'data': {'mes_err': e}}
                return JsonResponse(context)


class CreateContactView(ListView):
    def post(self, request, *args, **kwargs):
        chk_form_contact = CheckFormCreateContact(None)

        if request.POST.get('data_contact'):
            get_full_contact = json.loads(request.POST.get('data_contact'))

            print('full_contact =', get_full_contact, '-->', type(get_full_contact))
            chk_form_contact = CheckFormCreateContact(get_full_contact, request.FILES)

            if chk_form_contact.is_valid():
                print('true')
                Instance_contact = chk_form_contact.save(commit=False)
                Instance_contact.save()  

                print("get_all_queryset = ", get_full_contact) 
                context = {
                    'data': {
                        'data_contact': get_full_contact,
                    }
                }
                return JsonResponse(context)
            else:
                print('false')
                messages_error = chk_form_contact.errors.get_json_data(escape_html=True)
                context = {
                    'data':{
                        'data_invalid': get_full_contact,
                        'mes_err': messages_error
                    }
                }
                return JsonResponse(context)


class UpdateContactView(ListView):

    @transaction.atomic
    def get(self, request, id, *args, **kwargs):
        all_data = []
        get_contact_from_instance = ContactModel.objects.filter(contact_id=id).values().annotate(gender=F("gender__id"),nationality=F("nationality__id"))
        try:
            with transaction.atomic():
                get_alternate_email_from_instance = AlternateEmailModel.objects.select_related('contact_by').filter(contact_by=id, primary_status=True).values('alternate_email')
                get_alternate_phone_from_instance = AlternatePhoneModel.objects.select_related('contact_by').filter(contact_by=id, primary_status=True).values('alternate_phone')
                get_personal_address_from_instance = PersonalAddressModel.objects.select_related('contact_by').filter(contact_by=id, primary_status=True).values('address_1')
                print('get all obj success')
                print('alternate_email =', get_alternate_email_from_instance, '-->', type(get_alternate_email_from_instance))
                print('alternate_phone =', get_alternate_phone_from_instance, '-->', type(get_alternate_phone_from_instance))
                print('personal_address =', get_personal_address_from_instance, '-->', type(get_personal_address_from_instance))
                all_data = [
                    {'data_contact': list(get_contact_from_instance)},
                    {'data_alternate_email': list(get_alternate_email_from_instance)},
                    {'data_alternate_phone': list(get_alternate_phone_from_instance)},
                    {'data_personal_address': list(get_personal_address_from_instance)},
                ]
                context = {
                    'data': all_data,
                }
                return JsonResponse(context)

        except Exception as e:
            print("error get queryset = ", e)
            context = {
                'data': {
                    'mes_err': 'not found objects'
                } 
            }       
            return JsonResponse(context) 

    def post(self, request, id, *args, **kwargs):
        if request.POST.get('update_this_contact'):
            CheckFormCreateContact(None)
            get_new_data = json.loads(request.POST.get('update_this_contact'))
            get_contact_instance = ContactModel.objects.get(contact_id=id)
            chk_form = CheckFormCreateContact(get_new_data, request.FILES, instance=get_contact_instance)
            if chk_form.is_valid():
                print('true')
                set_instance = chk_form.save(commit=False)
                set_instance.save()

                context = {
                    'data': 'update contact success',
                }

                return JsonResponse(context)
            else:
                print('false')
                messages_error = chk_form.errors.get_json_data(escape_html=True)
                context = {
                    'data':{
                        'data_invalid': get_new_data,
                        'mes_err': messages_error
                    }
                }
                return JsonResponse(context)

class DeleteContactView(ListView):
    def post(self, request,id, *args, **kwargs):
        get_contact_id = id
        print(get_contact_id, '-->', type(get_contact_id))
        if get_contact_id is not None:
            try:
                get_contact_instance = get_object_or_404(ContactModel, contact_id=get_contact_id)
                get_contact_instance.delete()
                context = {
                    'data': 'delete contact success',
                }
                return JsonResponse(context)
            except Exception as e:
                print('delete contact failed | Error =', e)
                context = {
                    'data': 'delete contact failed',
                }
                return JsonResponse(context)


