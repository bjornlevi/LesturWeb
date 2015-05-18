#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy, sqlite3, os
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class Controller(object):

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['GET'])
    @cherrypy.tools.encode()
    def get_word(self):
        conn = sqlite3.connect('data/file_names.sqlite')
        c = conn.cursor()
        c.execute('''select * from file_names''')
        data = c.fetchall()
        print 'number of rows', len(data)

if __name__ == '__main__':
    config = {
            'global': {
                'server.socket_host': '0.0.0.0',
                'server.socket_port': 8080,
                'tools.encode.on': True,
                'tools.encode.encoding': 'utf-8',
                'log.screen': True
            },
            '/': {
                'tools.sessions.on': True,
                'tools.sessions.persistent': True,
                'tools.auth.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd()),
                'tools.sessions.on': True,
                'tools.sessions.timeout': 60
            },
                '/static': {
                'tools.staticdir.debug': True,
                'tools.staticdir.on': True,
                'tools.staticdir.dir': 'static'
        }
    }

    cherrypy.config.update(config)
    cherrypy.tree.mount(Controller(), '/', config = config)
    cherrypy.engine.start()
    cherrypy.engine.block()