from django.shortcuts import render, get_object_or_404
from index.models import Project, Cronjob, Database, Host


def project_detail(request, project_slug):
    return render(request, 'project_wiki.html',
                  {'project': get_object_or_404(Project, slug=project_slug)})


def cronjob_detail(request, cronjob_id):
    return render(request, 'cronjob_wiki.html',
                  {'cronjob': get_object_or_404(Cronjob, id=cronjob_id)})


def database_detail(request, database_id):
    return render(request, 'database_wiki.html',
                  {'database': get_object_or_404(Database, id=database_id)})


def host_detail(request, host_id):
    return render(request, 'host_wiki.html',
                  {'host': get_object_or_404(Host, id=host_id)})
