from django.shortcuts import render
from .models import Introduction
import re, mistune


# Create your views here.
def portfolio(request):
    """the portfolio of introduction pages"""
    if request.method == 'GET':
        # get the recommended introduction
        top_introduction = Introduction.objects.filter(is_recommend=1)

        method_flag = True

        context = {
            'top_introduction': top_introduction,
            'method_flag': method_flag
        }
        return render(request, "introduce/portfolio.html", context)
    else:
        method_flag = False
        context = {
            'method_flag': method_flag
        }
        return render(request, "introduce/portfolio.html", context)


# #################################################################################################
# Math Support refers to https://www.cnblogs.com/spaceskynet/p/13347938.html

class MathBlockGrammar(mistune.BlockGrammar):
    block_math = re.compile(r"^\$\$(.*?)\$\$", re.DOTALL)
    latex_environment = re.compile(r"^\\begin\{([a-z]*\*?)\}(.*?)\\end\{\1\}", re.DOTALL)


class MathBlockLexer(mistune.BlockLexer):
    default_rules = ['block_math', 'latex_environment'] + mistune.BlockLexer.default_rules

    def __init__(self, rules=None, **kwargs):
        if rules is None:
            rules = MathBlockGrammar()
        super(MathBlockLexer, self).__init__(rules, **kwargs)

    def parse_block_math(self, m):
        """Parse a $$math$$ block"""
        self.tokens.append({
            'type': 'block_math',
            'text': m.group(1)
        })

    def parse_latex_environment(self, m):
        self.tokens.append({
            'type': 'latex_environment',
            'name': m.group(1),
            'text': m.group(2)
        })


class MathInlineGrammar(mistune.InlineGrammar):
    math = re.compile(r"^\$(.+?)\$", re.DOTALL)
    block_math = re.compile(r"^\$\$(.+?)\$\$", re.DOTALL)
    text = re.compile(r'^[\s\S]+?(?=[\\<!\[_*`~\$]|https?://| {2,}\n|$)')


class MathInlineLexer(mistune.InlineLexer):
    default_rules = ['block_math', 'math'] + mistune.InlineLexer.default_rules

    def __init__(self, renderer, rules=None, **kwargs):
        if rules is None:
            rules = MathInlineGrammar()
        super(MathInlineLexer, self).__init__(renderer, rules, **kwargs)

    def output_math(self, m):
        return self.renderer.inline_math(m.group(1))

    def output_block_math(self, m):
        return self.renderer.block_math(m.group(1))


class MathRendererMixin(mistune.Renderer):
    def block_code(self, code, lang=None):
        code = code.rstrip('\n')
        if not lang:
            lang = 'text'
        code = mistune.escape(code, quote=True, smart_amp=False)
        return '<pre class="language-%s"><code class="language-%s">%s\n</code></pre>\n' % (lang, lang, code)

    def block_math(self, text):
        return '$$%s$$' % text

    def latex_environment(self, name, text):
        return r'\begin{%s}%s\end{%s}' % (name, text, name)

    def inline_math(self, text):
        return '$%s$' % text


class MarkdownWithMath(mistune.Markdown):
    def __init__(self, renderer, **kwargs):
        if 'inline' not in kwargs:
            kwargs['inline'] = MathInlineLexer
        if 'block' not in kwargs:
            kwargs['block'] = MathBlockLexer
        super(MarkdownWithMath, self).__init__(renderer, **kwargs)

    def output_block_math(self):
        return self.renderer.block_math(self.token['text'])

    def output_latex_environment(self):
        return self.renderer.latex_environment(self.token['name'], self.token['text'])

# #################################################################################################


def introduction_detail(request, id):
    """render introduction detail pages"""
    # get the introduction by its id
    top_introduction = Introduction.objects.get(id=id)
    # parse
    mk = MarkdownWithMath(renderer=MathRendererMixin())
    output = mk(r"{}".format(top_introduction.content))

    context = {
        'introduction': top_introduction,
        'introduction_detail_html': output,
    }
    return render(request, "introduce/introduction_detail.html", context)
