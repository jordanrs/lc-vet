from vet_site.course_info.models import InfoSetting

def common(request):
    LC_TELEPHONE = InfoSetting.objects.get(key="LUCY_CAV_TELEPHONE").value
    TECHNICAL_SUPPORT = InfoSetting.objects.get(key="TECHNICAL_SUPPORT").value
    return locals()