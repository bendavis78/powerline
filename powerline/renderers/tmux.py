# vim:fileencoding=utf-8:noet
# flake8: NOQA

from __future__ import absolute_import, unicode_literals

from powerline.renderer import Renderer
from powerline.colorscheme import ATTR_BOLD, ATTR_ITALIC, ATTR_UNDERLINE


class TmuxRenderer(Renderer):
    '''Powerline tmux segment renderer.'''

    character_translations = Renderer.character_translations.copy()
    character_translations[ord('#')] = '##[]'

    def hlstyle(self, fg=None, bg=None, attr=None):
        '''Highlight a segment.'''
        # We don't need to explicitly reset attributes, so skip those calls
        if not attr and not bg and not fg:
            return ''
        tmux_attr = []
        if fg is not None:
            if fg is False or fg[0] is False:
                tmux_attr += ['fg=default']
            else:
                tmux_attr += ['fg=colour' + str(fg[0])]
        if bg is not None:
            if bg is False or bg[0] is False:
                tmux_attr += ['bg=default']
            else:
                tmux_attr += ['bg=colour' + str(bg[0])]
        if attr is not None:
            if attr is False:
                tmux_attr += ['nobold', 'noitalics', 'nounderscore']
            else:
                if attr & ATTR_BOLD:
                    tmux_attr += ['bold']
                else:
                    tmux_attr += ['nobold']
                if attr & ATTR_ITALIC:
                    tmux_attr += ['italics']
                else:
                    tmux_attr += ['noitalics']
                if attr & ATTR_UNDERLINE:
                    tmux_attr += ['underscore']
                else:
                    tmux_attr += ['nounderscore']
        return '#[' + ','.join(tmux_attr) + ']'

#   def get_segment_info(self, segment_info, mode):
#       r = self.segment_info.copy()
#       if segment_info:
#           r.update(segment_info)
#       if 'pane_id' in r:
#           varname = 'TMUX_PWD_' + r['pane_id'].lstrip('%')
#           if varname in r['environ']:
#               r['getcwd'] = lambda: r['environ'][varname]
#       r['mode'] = mode
#       return r

    def get_segment_info(self, segment_info, mode):
        r = self.segment_info.copy()
        if segment_info:
            r.update(segment_info)
       # pane_info = r.pop('pane_info', None)
       # if pane_info:
       #     varnames = ['pane_id', 'pane_current_path']
       #     r.update(zip(varnames, pane_info.split('|')))
       #     r['getcwd'] = lambda: r['pane_current_paht']
        r['mode'] = mode
        return r


renderer = TmuxRenderer
