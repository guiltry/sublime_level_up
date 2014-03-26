import sublime, sublime_plugin

class LevelUpCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		beginningOfFile = False

		FirstEnd = self.view.line(self.view.sel()[0])
		row, lastIndent = self.view.rowcol(FirstEnd.a)
		
		while True:
			newline, newIndent = self.moveRight(row, 0)
			
			if not newline:
				if lastIndent == 0 and not beginningOfFile:
					lastIndent = newIndent;
				elif lastIndent > newIndent or beginningOfFile:
					self.view.sel().clear()
					self.view.sel().add(sublime.Region(self.view.text_point(row, newIndent)))
					self.view.show(self.view.text_point(row, newIndent))
					break
			if row != 0:
				row -= 1;
			else:
				beginningOfFile = True

	def moveRight(self, r, c):
		while True:
			temp = self.view.text_point(r, c)
			if self.view.substr(temp) == '\n':
				return True, 0
			if self.view.substr(temp) == '\t' or self.view.substr(temp) == ' ':
				c += 1
			else: 
				return False, c