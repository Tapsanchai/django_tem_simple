jQuery(function()
{
    jQuery(document).on('show.bs.modal', '.modal', function()
    {
        var maxZ = parseInt(jQuery('.modal-backdrop').css('z-index')) || 1040;

        jQuery('.modal:visible').each(function()
        {
            maxZ = Math.max(parseInt(jQuery(this).css('z-index')), maxZ);
        });

        jQuery('.modal-backdrop').css('z-index', maxZ);
        jQuery(this).css("z-index", maxZ + 1);
        jQuery('.modal-dialog', this).css("z-index", maxZ + 2);
    });

    jQuery(document).on('hidden.bs.modal', '.modal', function () 
    {
        if (jQuery('.modal:visible').length)
        {
            jQuery(document.body).addClass('modal-open');

           var maxZ = 1040;

           jQuery('.modal:visible').each(function()
           {
               maxZ = Math.max(parseInt(jQuery(this).css('z-index')), maxZ);
           });

           jQuery('.modal-backdrop').css('z-index', maxZ-1);
       }
    });
});