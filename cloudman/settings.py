#coding=utf8
import os.path
import tornado.web

import handlers
import modules

URLS = [
    (r"/signin/", handlers.SignInHandler),
    (r"/signout/", handlers.SignOutHandler),
    (r"/signup/", handlers.SignUpHandler),
    
    (r'/', handlers.IndexHandler),
    
    (r'/instances/', handlers.InstancesHandler),
    (r'/instances/([\w-]+)/', handlers.InstanceViewTextHandler),
    (r'/instances/([\w-]+)/view/text/', handlers.InstanceViewTextHandler),
    (r'/instances/([\w-]+)/view/graph/', handlers.InstanceViewGraphHandler),
    
    (r'/volumes/', handlers.VolumesHandler),
    
    (r'/networks/', handlers.RoutersHandler),
    (r'/networks/routers/', handlers.RoutersHandler),
    (r'/networks/vxnets/', handlers.VxnetsHandler),
    
    (r'/eips/', handlers.EipsHandler),
    (r'/eips/([\w-]+)/', handlers.EipViewHandler),
    
    (r'/security_groups/', handlers.SecuritygroupsHandler),
    (r'/security_groups/([\w-]+)/', handlers.SecuritygroupViewHandler),
    
    (r'/keypairs/', handlers.KeypairsHandler),
    (r'/keypairs/([\w-]+)/', handlers.KeypairViewHandler),
    
    (r'/images/', handlers.ImagesPublicHandler),
    (r'/images/system/', handlers.ImagesPublicHandler),
    (r'/images/system/([\w-]+)/', handlers.ImagePublicViewHandler),
    (r'/images/self/', handlers.ImagesPrivateHandler),
    (r'/images/self/([\w-]+)/', handlers.ImagePrivateViewHandler),
    
    (r'/activities/', handlers.ActivitiesHandler),
    (r'/activities/all/', handlers.ActivitiesHandler),
    
    (r'/consumptions/', handlers.ConsumptionsSummaryHandler),
    (r'/consumptions/summary/', handlers.ConsumptionsSummaryHandler),
    (r'/consumptions/query/', handlers.ConsumptionsQueryHandler),
    
    (r'/tickets/', handlers.TicketsHandler),
    
    (r'/access_keys/', handlers.AccesskeysHandler),

]

APPLICATION_SETTINGS = dict(
    site_name='Cloud Man',
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    ui_modules={"SideBars": modules.SideBarsModule},
    xsrf_cookies=True,
    #gzip=True,
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url="/signin/",
    debug=True,
)

PORT = 80

SERVER_IP = '125.64.8.251'

PROJECT_ID = '964fea5a29b441b1a5b768ed38c2a6a3'

PROJECT_NAME = 'demo'

ADMIN_USER = 'admin'
ADMIN_PASS = ''

AUTH_URLS = dict(
    cinder = 'http://%s:8776/v1/%s' % (SERVER_IP, PROJECT_ID),
    glance = 'http://%s:9292/v2' % SERVER_IP,
    nova = 'http://%s:8774/v2/%s' % (SERVER_IP, PROJECT_ID),
    ec2 = 'http://%s:8773/services/Cloud' % SERVER_IP,
    keystone = 'http://%s:5000/v2.0' % SERVER_IP,
)

SIDEBARS = {'Member':[
    dict(
        url='/dashboard/',
        icon='dashboard',
        name='控制台',
    ),
    dict(
        url='/instances/',
        icon='dashboard',
        name='虚拟机',
    ),
    dict(
        url='/volumes/',
        icon='dashboard',
        name='磁盘存储',
    ),
    dict(
        url='/snapshots/',
        icon='dashboard',
        name='快照备份',
    ),
    dict(
        url='/images/',
        icon='dashboard',
        name='系统镜像',
    ),
    dict(
        url='/flavors/',
        icon='dashboard',
        name='硬件配置',
    ),
]}

SIDEBARS['Manager'] = SIDEBARS['Member'] + []

SIDEBARS['Admin'] = SIDEBARS['Manager'] + []