import sublime, sublime_plugin
import re

class NumberPasteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        clip = sublime.get_clipboard()
        if re.search('\$\d+\$', clip):
            #$$の部分を外してからペースト
            paste = re.sub('\$(\d+)\$', r'\1', clip)
            self.view.replace(edit, self.view.sel()[0], paste)
            sels.clear()
            #$$の中身を1づつ増やす
            #数字が違うものが混ざっているかもしれないから、慎重に
            #tmp = re.split('\$(\d+)\$', clip)


        else:
            #そのままコピー
            self.view.replace(edit, self.view.sel()[0], clip)
            sels.clear()

