from annotations.annotator_access import RemoteAnnotator

url = "https://krono.act.uji.es/annotator/cmr-qa/"
params = {'q': 'fat water cancellation'}

RemoteAnnotator(url, params)
#LocalTKBGAnnotator()

