# str1 = '<i><zgpvh><u><w></w></u><rcojp><mkqg></mkqg></rcojp><y></y></zgpvh><jsbqa></jsbqa></i><vwi><xpv><bdn><lvd><u></u><rb><zza></zza></rb><brjca></brjca></lvd><s><tchq><ya></ya><lb><d></d><tkav></tkav><uxfr><g></g></uxfr><vv></vv></lb><te></te><ooq><c></c></ooq><kirpl></kirpl></tchq><zxx></zxx><x></x><a></a></s><mu><jqi></jqi></mu><olmwh></olmwh></bdn><yrcc></yrcc><lqzt><qup></qup></lqzt><qqc></qqc></xpv><ejg><o></o></ejg><ldm><mvhen><du></du></mvhen><l></l><tx></tx></ldm><xdyg><g><nl></nl><hwbpl></hwbpl></g<<b><h><o><ggs></ggs><unt></unt></o><vdse></vdse></h><yfqjs></yfqjs><kxcye></kxcye></b><aol></aol></xdyg><hfhrp></hfhrp></vwi><g><ovly><yudv></yudv><qe></qe></ovly><h><ayk></ayk><em></em></h><lglx></lglx></g><mk><a></a></mk><efh></efh>'

str1 = '<a/</a>'

symbols = 'abcdefghijklmnopqrstuvwxyz</>'

breaket_counter = 0
tag_stack = []
for i in range(len(str1)):
    for char in symbols:
        new_str = str1[:i] + char + str1[i+1:]
        broken = False
        curent_tag = ''
        close_tag = False
        tag_stack = []
        breaket_counter = 0
        for char in new_str:
            curent_tag += char
            if char == '<':
                waiting_close = True
                if breaket_counter !=0:
                    broken = True
                    break
                breaket_counter = 1
            if char == '/':
                close_tag = True
            elif char == '>':
                if breaket_counter != 1:
                    broken = True
                    break
                breaket_counter = 0
                if waiting_close:                
                    if close_tag:
                        if tag_stack:
                            stack_tag = tag_stack.pop()
                            if (stack_tag[0:1] + '/' + stack_tag[1:]) != curent_tag:
                                broken = True
                                break
                        else:
                            broken = True
                            break
                        close_tag = False
                    else:
                        tag_stack.append(curent_tag)
                    waiting_close = False
                    curent_tag = ''
        if breaket_counter !=0 or tag_stack:
            broken = True
        if not broken:
            break
    if not broken:
            break

print(new_str)


        


