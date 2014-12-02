def cigar_party(cigars, is_weekend):
    if cigars >= 40 and cigars <= 60:
        return True
    elif cigars >= 40 and is_weekend:
        return True
    else:
        return False

print cigar_party(30,False)
print cigar_party(50,False)
print cigar_party(70,True)


def make_tags(tag,text):
    html = '<'+ tag +'>'
    html = html + text
    html = html + '</' + tag + '>'
    return html
print make_tags('i',"luke is alwsome")
