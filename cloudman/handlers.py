#coding=utf8
import tornado.web
import tornado.escape
import settings
from pprint import pprint as pp
from novaclient.v1_1 import client as nova_client
from keystoneclient.v2_0 import client as keystone_client

class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        pass

    def get_current_user(self):
        return self.get_secure_cookie('user')

    def get_flash(self):
        flash = self.get_secure_cookie('flash')
        self.clear_cookie('flash')
        return flash

    @property
    def client(self):
        user = self.get_secure_cookie('user')
        token = self.get_secure_cookie('token')
        c = nova_client.Client(user, token, project_id=settings.PROJECT_ID, auth_url=settings.AUTH_URLS['nova'])
        c.client.auth_token = token
        c.client.management_url = settings.AUTH_URLS['nova']
        return c

class SignInHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            self.redirect('/')
            return
        self.render('signin.html', notification=self.get_flash())

    def post(self):
        user = self.get_argument('user')
        password = self.get_argument('password')
        try:
            k = keystone_client.Client(username=user, password=password, project_id=settings.PROJECT_ID, auth_url=settings.AUTH_URLS['keystone'])
        except Exception , e:
            self.set_secure_cookie('flash', e.message)
            self.redirect('/signin/')
            return
        token = k.auth_ref['token']['id']
        self.set_secure_cookie('user', user)
        self.set_secure_cookie('token', token)
        self.redirect(self.get_argument('next', '/'))

class SignOutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.clear_cookie('token')
        self.redirect('/')

class SignUpHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            self.redirect('/')
            return
        self.render('signup.html', notification=self.get_flash())

    def post(self):
        user = self.get_argument('user')
        password = self.get_argument('password')
        try:
            k = keystone_client.Client(username=settings.ADMIN_USER, password=settings.ADMIN_PASS, project_id=settings.PROJECT_ID, auth_url=settings.AUTH_URLS['keystone'])
            newuser = k.users.create(user, password, '%s@test.com' % user, tenant_id=settings.PROJECT_ID, enabled=True)
            member_role_id = k.roles.find(name='Member').id
            k.tenants.add_user(settings.PROJECT_ID, newuser.id, member_role_id)
            k = keystone_client.Client(username=user, password=password, project_id=settings.PROJECT_ID, auth_url=settings.AUTH_URLS['keystone'])
        except Exception , e:
            self.set_secure_cookie('flash', e.message)
            self.redirect('/signup/')
            return
        token = k.auth_ref['token']['id']
        self.set_secure_cookie('user', user)
        self.set_secure_cookie('token', token)
        self.redirect(self.get_argument('next', '/'))

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        kwargs = dict(page_title='首页')
        self.render('index.html', **kwargs)

class InstancesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        kwargs = dict(page_title='主机')
        instances = self.client.servers.list()
        kwargs['instances'] = instances
        fr
        self.render('instances.html', **kwargs)

class VolumesHandler(BaseHandler):
    def get(self):
        kwargs = dict(page_title='硬盘')
        volumes = self.client.volumes.list()
        kwargs['volumes'] = volumes
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
        floating_ips = self.client.floating_ips.list()
        kwargs['floating_ips'] = floating_ips
        self.render('eips.html', **kwargs)

class SecuritygroupsHandler(BaseHandler):
    def get(self):
        kwargs = dict(page_title='防火墙')
        security_groups = self.client.security_groups.list()
        kwargs['security_groups'] = security_groups
        self.render('security_groups.html', **kwargs)

class KeypairsHandler(BaseHandler):
    def get(self):
        kwargs = dict(page_title='SSH密钥')
        keypairs = self.client.keypairs.list()
        kwargs['keypairs'] = keypairs
        self.render('keypairs.html', **kwargs)

class ImagesPublicHandler(BaseHandler):
    def get(self):
        kwargs = dict(page_title='系统映像')
        images = self.client.images.list()
        kwargs['images'] = images
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