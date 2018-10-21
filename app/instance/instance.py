# -*- coding: utf-8 -*-
'''
>file name:instance.py
>author:shakey
>create time :2018/10/18  2:13 PM
'''
from flask import request, flash, render_template, redirect, url_for
from .forms import CreateInstanceForm
from app.docker_client.docker_ops import DockerClient
from .schema import InstanceSchema
def create_instace():
    form=CreateInstanceForm()
    if request.method=='POST' and form.validate_on_submit():
        image=form.image.data
        port = {"3306/tcp": form.data.get("port")}
        volumes = form.volumes.data.split(",")
        print ('开始执行docker')
        with DockerClient() as docker:
            print(image, port, volumes)
            docker.run(image, ports=port, volumes=volumes)
        flash(u'you create a instance')
        return redirect(url_for('dashboard_manage.index'))
    return render_template('create_instance.html',form=form)

def list_instance():
    comments = []
    with DockerClient() as docker:
        containers = docker.list_containers()
        for container in containers:
            try:
                instance = InstanceSchema().load(
                    {"name": container.image.tags[0], "short_id": container.short_id, "status": container.status,
                     "created": container.attrs.get("Created")})
            except:
                # todo fix
                instance = InstanceSchema().load(
                    {"name": 'xxx', "short_id": container.short_id, "status": "xxx",
                     "created": "xxx"})

            comments.append(instance.data)
    return render_template('list_instance.html',comments=comments)

def restart_instance():

    return 'stop instance'

def stop_instance(instance_id):
    with DockerClient() as docker:
        if instance_id == "Dangerous_All":
            docker.stop("", stop_all=True)
            flash("Stop All Instance Success.")
        elif docker.stop(instance_id):
            flash("Stop Success.")
        else:
            flash("Stop Failed.")
    return  redirect(url_for('dashboard_manage.index'))
def list_image():
    with DockerClient() as docker:
        pass
