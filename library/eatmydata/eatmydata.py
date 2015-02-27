"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class eatmydata(ShutItModule):


	def build(self, shutit):
		shutit.install('eatmydata')
		shutit.run_script(r"""
cat >> ${HOME}/.bashrc << END
bind 'RETURN: "\e[1~eatmydata \e[4~\n"'
END
""")
		shutit.run_script(r"""
cat >> /etc/bash.bashrc << END
bind 'RETURN: "\e[1~eatmydata \e[4~\n"'
END
""")
		shutit.run_script(r"""
cat >> /etc/profile << END
bind 'RETURN: "\e[1~eatmydata \e[4~\n"'
END
""")
		shutit.login()
		shutit.pause_point('')
		return True

def module():
	return eatmydata(
		'shutit.tk.eatmydata.eatmydata', 0.0000001,
		description='Speed up your builds by including this module',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)

