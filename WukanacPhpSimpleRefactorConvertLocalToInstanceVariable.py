import sublime, sublime_plugin
import subprocess
import tempfile
import os

from WukanacPhpSimpleRefactor.WukanacPhpSimpleRefactorBase import WukanacPhpSimpleRefactorBaseCommand

class WukanacPhpSimpleRefactorConvertLocalToInstanceVariableCommand(WukanacPhpSimpleRefactorBaseCommand):
	old_name = '';

	def process(self):
		sublime.active_window().show_input_panel('Variable name', '', self.obtain_old_name, None, None)

	def obtain_old_name(self, name):
		self.old_name = name;
		self.on_filled_info()

	def get_command(self):
		settings = sublime.load_settings('WukanacPhpSimpleRefactor.sublime-settings')
		self.php_path = settings.get('php_path')
		self.refactor_path = settings.get('refactor_path')
		
		rows = str(self.rowBegin)
		# php refactor.phar convert-local-to-instance-variable <file> <line> <variable>
		cmd = ''.join([self.php_path, ' "', self.refactor_path,'" ',  'convert-local-to-instance-variable', ' "', self.file_name, '" ', rows, ' ', self.old_name])
		print(cmd)
		return subprocess.Popen(cmd, shell=True, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
