from jeopardy import config, rows

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
from urllib.parse import urlencode
import json, random

state = ''
# TODO: Persist player scores (in memory and in save)

class GMHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)

	def do_HEAD(self):
		self.send_response(200)

	def do_POST(self):
		content_length = int(self.headers['Content-Length']) 
		post_data = self.rfile.read(content_length)
		self.send_response(200)
		self.reply(post_data)

	def reply(self, post_data):
		global state
		d = json.loads(post_data.decode('utf-8'))
		if d['text'].lower().startswith(config['Options']['GroupMeCommand']):
			if state == '':
				category, value, question, answer = random.choice(rows)[3:7]
				post_message('%s: %s' % (category, question))
				state = answer
			else:
				post_message('ANSWER: %s' % (state))
				state = ''


def post_message(message):
	req = urlencode({ 
		'bot_id': config['Options']['GroupMeBotID'], 
		'text': message
	})
	urlopen(config['Options']['GroupMeAPI'], bytes(req, 'utf-8'))

if __name__ == "__main__":
	address = (config['Options']['GroupMeHost'], \
		int(config['Options']['GroupMePort']))
	handler = GMHandler
	httpd = HTTPServer(address, handler)
	print('Listening on port', address[1])
	httpd.serve_forever()

