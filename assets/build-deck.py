#!/usr/bin/env python3
"""deck-template.html + joint-decision-ui.html -> deck.html

프로토타입을 <script type="text/plain"> 에 인라인한다.
srcdoc 으로 주입하면 부모와 same-origin 이라 contentDocument 로 스텝을 지정할 수 있다.
(data: URI 는 opaque origin 이라 그게 안 된다)
"""
import pathlib, sys

here = pathlib.Path(__file__).parent
tpl   = (here / 'deck-template.html').read_text(encoding='utf-8')
proto = (here / 'joint-decision-ui.html').read_text(encoding='utf-8')

if '__PROTO__' not in tpl:
    sys.exit('deck-template.html 에 __PROTO__ 플레이스홀더가 없다')

# 원문의 </script> 만 깨뜨리므로 그것만 이스케이프. 주입 시 JS 가 되돌린다.
out = tpl.replace('__PROTO__', proto.replace('</script>', '<\\/script>'))
(here / 'deck.html').write_text(out, encoding='utf-8')
n = out.count('<section class="slide')
print(f'deck.html {len(out)//1024}KB · 슬라이드 {n}장')
