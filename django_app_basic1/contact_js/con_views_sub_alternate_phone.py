from django.db import models
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
# import json_tricks

from django.core.serializers.json import DjangoJSONEncoder
# from django.core.serializers import serialize

from .con_models import AlternatePhoneModel
from .con_alternate_p_form_control import CheckFormCreateAlternatePhone


class CreateOrUpdateAlternatePhoneView(ListView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('con_id'):
            get_contact_id = int(request.GET.get('con_id'))
            print("get_contact_id = ", get_contact_id)
            if get_contact_id:
                get_alternate_phone_from_instance = AlternatePhoneModel.objects.select_related('contact_by','phone_type').filter(contact_by=get_contact_id).values(
                    'id','alternate_phone','contact_by','description','primary_status','phone_type').annotate(phone_type_title=F("phone_type__type_title")).order_by('-primary_status')
                context = {
                    'data': {
                        'data_alternate_phone': list(get_alternate_phone_from_instance),
                    }
                }
                return JsonResponse(context)
            else:
                pass


    @transaction.atomic
    def post(self, request,id, *args, **kwargs):
        chk_form_alternate_phone = CheckFormCreateAlternatePhone(None)
        build_get_id = id
        if request.POST.get('update_alternate_phone'):
            get_data_alternate_phone = json.loads(request.POST.get('update_alternate_phone'))

            print('get_data_alternate_phone =', get_data_alternate_phone, '-->', type(get_data_alternate_phone))
            if build_get_id is not None:
                print('get ID =', build_get_id, '-->', type(build_get_id))
                get_instance_object = AlternatePhoneModel.objects.select_related('contact_by','phone_type')
                print('get_instance_object: ', get_instance_object.get(id=build_get_id))

                chk_form_alternate_phone = CheckFormCreateAlternatePhone(get_data_alternate_phone, instance=get_instance_object.get(id=build_get_id))
                if chk_form_alternate_phone.is_valid():
                    print('true')
                    instance_alternate_phone = chk_form_alternate_phone.save(commit=False)
                    instance_alternate_phone.save()
                    get_contact_by = instance_alternate_phone.contact_by
                    try:
                        get_alternate_phone_from_instance = get_instance_object.filter(contact_by=get_contact_by).values(
                        'id','alternate_phone','contact_by','description','primary_status','phone_type').annotate(phone_type_title=F("phone_type__type_title")).order_by('-primary_status')
                        print('update success')
                        context = {
                            'data': {
                                'data_alternate_phone': list(get_alternate_phone_from_instance),
                            }
                        }
                        return JsonResponse(context)
                    except Exception as error:
                        print(error)

                else:
                    print('false')
                    messages_error = chk_form_alternate_phone.errors.get_json_data(escape_html=True)
                    context = {
                        'data': {
                            'data_invalid': get_data_alternate_phone,
                            'mes_err': messages_error
                        }
                    }
                    return JsonResponse(context)

        elif request.POST.get('create_alternate_phone'):
            get_data_alternate_phone = json.loads(request.POST.get('create_alternate_phone'))

            print('get_data_alternate_phone =', get_data_alternate_phone, '-->', type(get_data_alternate_phone))
            chk_form_alternate_phone = CheckFormCreateAlternatePhone(get_data_alternate_phone)
            if chk_form_alternate_phone.is_valid():
                print('true')
                instance_alternate_phone = chk_form_alternate_phone.save(commit=False)
                instance_alternate_phone.save()
                get_instance_object = AlternatePhoneModel.objects.select_related('contact_by','phone_type')
                try:
                    get_alternate_phone_from_instance = get_instance_object.filter(contact_by=build_get_id).values(
                    'id','alternate_phone','contact_by','description','primary_status','phone_type').annotate(phone_type_title=F("phone_type__type_title")).order_by('-primary_status')
                    print('create success')
                    context = {
                        'data': {
                            'data_alternate_phone': list(get_alternate_phone_from_instance),
                        }
                    }
                    return JsonResponse(context)
                except Exception as error:
                    print(error)
            else:
                print('false')
                messages_error = chk_form_alternate_phone.errors.get_json_data(escape_html=True)
                
                context = {
                    'data': {
                        'data_invalid': get_data_alternate_phone,
                        'mes_err': messages_error,
                        'mes_err2': messages_error
                    }
                }
                return JsonResponse(context)

        elif request.POST.get('this_alternate_phone'):
            get_data_contact_by = json.loads(request.POST.get('this_alternate_phone'))
            print('build_get_id =',build_get_id);
            print('get_data_alternate_phone_id =', get_data_contact_by, '-->', type(get_data_contact_by))

            get_instance_object = AlternatePhoneModel.objects.select_related('contact_by','phone_type')
            this_item = get_instance_object.filter(id=build_get_id)
            this_chk_status = this_item.values('primary_status')
            try:
                for item in this_chk_status:
                    print('primary_status= ', item['primary_status'])
                    get_primary_status = item['primary_status']
                if get_primary_status is not True:
                    this_item.update(primary_status=True)
                    with transaction.atomic():
                        get_instance_object.filter(contact_by=get_data_contact_by, primary_status=True).exclude(id=build_get_id).update(primary_status=False)
                        try:
                            get_alternate_phone_from_instance = get_instance_object.filter(contact_by=get_data_contact_by).values(
                            'id','alternate_phone','contact_by','description','primary_status','phone_type').annotate(phone_type_title=F("phone_type__type_title")).order_by('-primary_status')
                            print('update status success')
                            context = {
                                'data': {
                                    'data_alternate_phone': list(get_alternate_phone_from_instance),
                                }
                            }
                            return JsonResponse(context)
                        except Exception as error:
                            print('get new alternate_phone is error =', error)
                else:
                    mes = 'Defualt Status is True'
                    get_alternate_phone_from_instance = get_instance_object.filter(contact_by=get_data_contact_by).values(
                    'id','alternate_phone','contact_by','description','primary_status','phone_type').annotate(phone_type_title=F("phone_type__type_title")).order_by('-primary_status')
                    print('NOT update status')
                    context = {
                        'data': {
                            'mes': mes,
                            'data_alternate_phone': list(get_alternate_phone_from_instance),
                        }
                    }
                    return JsonResponse(context)
            except Exception as e:
                print("Change Status Error =", e)

class DeleteAlternatePhoneView(ListView):
    def post(self, request, id, *args, **kwargs):
        if request.POST.get('data_by_contact_id'):
            get_contact_by_id = request.POST.get('data_by_contact_id')
            get_alternate_id = id
            print(get_alternate_id, '-->', type(get_alternate_id))
            if get_alternate_id is not None:
                try:
                    get_alternate_phone_instance = get_object_or_404(AlternatePhoneModel, id=get_alternate_id)
                    get_alternate_phone_instance.delete()
                    get_instance_object = AlternatePhoneModel.objects.select_related('contact_by','phone_type')
                    get_alternate_phone_from_instance = get_instance_object.filter(contact_by=get_contact_by_id).values(
                    'id','alternate_phone','contact_by','description','primary_status','phone_type').annotate(phone_type_title=F("phone_type__type_title")).order_by('-primary_status')
                    print('create success')
                    context = {
                        'data': {
                            'data_alternate_phone': list(get_alternate_phone_from_instance),
                            'mes_success': 'delete alternate_phone success',
                        }
                    }
                    return JsonResponse(context)
                except Exception as e:
                    print('delete alternate_phone failed | Error =', e)
                    context = {
                        'data': {
                            'mes_err': 'delete alternate_phone failed',
                        }
                    }
                    return JsonResponse(context)
