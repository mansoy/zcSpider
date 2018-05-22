def fb_kwin4qnum(jq,sq,rq=0):
    if (jq<0)or(sq<0):return -1
    #
    jqk=jq+rq  #or -rq
    if jqk>sq:kwin=3
    elif jqk<sq:kwin=0
    else:kwin=1
    #
    return kwin