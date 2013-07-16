# -*- coding: UTF-8 -*-

import sublime, sublime_plugin
import re

class NumberPasteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #クリップボードの中身を取得する
        clip = sublime.get_clipboard()
        #選択中の文字列を取得する(複数選択は未対応)
        select_txt = self.view.substr(self.view.sel()[0])
        #書式が連番指定になっているか調べる
        m = re.match('(\d+)-(\d+)',select_txt)
        if m:
            #書式が正しいので、番号を書き換えながら連続ペーストする
            #開始番号
            start = int(m.group(1))
            #終了番号
            end = int(m.group(2))
            #開始番号1文字目が0の場合、足りない桁をゼロで埋めてから書き出す
            #桁数は開始番号のものを参照
            if m.group(1)[0] == '0':
                zero_padding = len(m.group(1))
            else:
                zero_padding = 0

            paste = "";
            for i in range(start,end+1):
                #桁数ゼロ
                if len(str(i)) > zero_padding:
                    num = str(i)
                else:
                    num = str(i).zfill(zero_padding)
                paste += clip.replace('$$$', num) + "\n"
            #最後にまとめてペースト
            self.view.replace(edit, self.view.sel()[0], paste)
        else:
            #想定する書式と違っているので、何もせず終了
            #(エラーメッセージを出したい。英語で、日本人にもわかりそうなのを)
            pass



