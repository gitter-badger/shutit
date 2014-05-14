#Copyright (C) 2014 OpenBet Limited
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is furnished
#to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from shutit_module import ShutItModule
import util

class get_iplayer(ShutItModule):

	def is_installed(self,shutit):
		return False

	def build(self,shutit):
		shutit.set_default_expect(shutit.cfg['expect_prompts']['root_prompt'])
		shutit.install('git')
		shutit.install('liblwp-online-perl')
		shutit.install('rtmpdump')
		shutit.install('ffmpeg')
		shutit.install('mplayer')
		shutit.install('atomicparsley')
		shutit.install('id3v2')
		shutit.install('libmp3-info-perl')
		shutit.install('libmp3-tag-perl')
		shutit.install('libnet-smtp-ssl-perl')
		shutit.install('libnet-smtp-tls-butmaintained-perl')
		shutit.install('libxml-simple-perl')
		shutit.send_and_expect('git clone git://git.infradead.org/get_iplayer.git')
		shutit.send_and_expect('cd get_iplayer')
		shutit.send_and_expect('chmod 755 get_iplayer')
		shutit.send_and_expect('./get_iplayer')
		return True

if not util.module_exists('shutit.tk.get_iplayer.get_iplayer'):
	obj = get_iplayer('shutit.tk.get_iplayer.get_iplayer',0.324,'iPlayer downloader. See http://www.infradead.org/get_iplayer/html/get_iplayer.html')
	obj.add_dependency('shutit.tk.setup')
	util.get_shutit_modules().add(obj)
	ShutItModule.register(get_iplayer)
