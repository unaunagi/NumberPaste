# -*- coding: UTF-8 -*-

import sublime, sublime_plugin
import re

class NumberPasteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #クリップボードの中身を取得する
        clip = sublime.get_clipboard()
        #選択中の文字列を取得する(複数選択は未対応)
        select_txt = self.view.substr(self.view.sel()[0])
        #書式が正しいか調べる
        m = re.match('(\d+)-(\d+)',select_txt)
        if m:
            #書式は正しいので、番号を書き換えながら連続ペーストする
            start = int(m.group(1))
            end = int(m.group(2))
            paste = "";
            for i in range(start,end+1):
                paste += clip.replace('$$$', str(i))
            #最後にまとめてペースト
            self.view.replace(edit, self.view.sel()[0], paste)
        else:
            #想定する書式と違っていたら、何もせず終了
            #(エラーメッセージを出したい。英語で、日本人にもわかりそうなのを)
            pass



