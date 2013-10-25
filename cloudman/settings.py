#coding=utf8
import os.path
import tornado.web

import handlers
import modules

URLS = [
	(r'/', handlers.IndexHandler),
	
	(r'/instances/', handlers.InstancesHandler),
	
	(r'/volumes/', handlers.VolumesHandler),
	
	(r'/networks/', handlers.RoutersHandler),
	(r'/networks/routers/', handlers.RoutersHandler),
	(r'/networks/vxnets/', handlers.VxnetsHandler),
	
	(r'/eips/', handlers.EipsHandler),
	
	(r'/security_groups/', handlers.SecuritygroupsHandler),
	
	(r'/keypairs/', handlers.KeypairsHandler),
	
	(r'/images/', handlers.ImagesPublicHandler),
	(r'/images/system/', handlers.ImagesPublicHandler),
	(r'/images/self/', handlers.ImagesPrivateHandler),
	
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
	#xsrf_cookies=True,
	#gzip=True,
	cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
	login_url="/login/",
	debug=True,
)

PORT = 80

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