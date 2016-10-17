import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class City(object):
    def __init__(self, name, country, picture):
        self.name = name
        self.picture = picture
        self.country = country

cities = [City(name="Vienna", country="Austria", picture="http://www.airpano.ru/files/Vienna-Austria/images/image4.jpg")]


class MainHandler(BaseHandler):
    def get(self):
        city = cities[0]
        return self.render_template("hello.html", params={"picture": city.picture, "country": city.country})

    def post(self):
        x = self.request.get("x")
        if x == cities[0].name:
            return self.write("Congrats! You guessed it")
        elif x != cities[0].name:
            self.write("You are wrong! Try again")
            return self.render_template("hello.html", params={"picture": City.picture, "country": City.country})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)# Calculator_Post_Request
# Casino_post_request
# Casino_post_request
# Casino_Post_Request
# Game_capital_country
