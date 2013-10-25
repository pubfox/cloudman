#coding=utf8
import tornado.web
from novaclient.v1_1.client import Client

class BaseHandler(tornado.web.RequestHandler):
	@property
	def globalvar(self):
		return self.application.globalvar
		
	def initialize(self):
		print 'init'
		
	def prepare(self):
		#self.client = Client('admin', 'admin_pass', 'admin', 'http://192.168.1.200:5000/v2.0')
		pass
		
	def on_finish(self):
		print 'on_finish'
		
	def get_current_user(self):
		return dict(name='test', role='Member')

class IndexHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='首页')
		self.render('index.html', **kwargs)

class InstancesHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='主机')
		self.render('instances.html', **kwargs)

class VolumesHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='硬盘')
		self.render('volumes.html', **kwargs)

class RoutersHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='路由器')
		self.render('routers.html', **kwargs)

class VxnetsHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='私有网络')
		self.render('vxnets.html', **kwargs)

class EipsHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='公网IP')
		self.render('eips.html', **kwargs)

class SecuritygroupsHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='防火墙')
		self.render('security_groups.html', **kwargs)

class KeypairsHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='SSH密钥')
		self.render('keypairs.html', **kwargs)

class ImagesPublicHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='系统映像')
		self.render('images.public.html', **kwargs)

class ImagesPrivateHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='自有映像')
		self.render('images.private.html', **kwargs)

class ActivitiesHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='操作日志')
		self.render('activities.html', **kwargs)

class ConsumptionsSummaryHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='消费记录摘要')
		self.render('consumptions.summary.html', **kwargs)

class ConsumptionsQueryHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='消费记录查询')
		self.render('consumptions.query.html', **kwargs)

class TicketsHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='工单')
		self.render('tickets.html', **kwargs)

class AccesskeysHandler(BaseHandler):
	def get(self):
		kwargs = dict(page_title='API密钥')
		self.render('access_keys.html', **kwargs)