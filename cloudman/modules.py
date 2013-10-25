#coding=utf8
import tornado.web
import settings

class SideBarsModule(tornado.web.UIModule):
	def render(self, user):
		role = getattr(user, 'role', 'Member')
		sidebars = settings.SIDEBARS.get(role, settings.SIDEBARS.get('Member'))
		return self.render_string("modules/sidebars.html", sidebars=sidebars)