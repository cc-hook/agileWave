
import re
#==================================================
wavedrom_signal_define = '''{{"name":"{sig_name}","wave":"{wave_str}","data":"{data_str}","node":"{node_str}"}}'''
#==================================================
# wavedrom_code = '''{{"signal":[
# {sig_str}]
# }}'''
wavedrom_code = '''{{"signal":[
{sig_str}],
"edge":{edge_str}
}}'''
#==================================================
def extractSignal(sig_list):
    rtn_list = []
    edge_list = []
    for iter_str in sig_list:
        obj = re.match(r'(\w+)\s*:\s*(.+);', iter_str)
        if obj is None: continue
        sig_name = obj.group(1)
        split_list = obj.group(2).split()
        [wave_str,data_str,edge_str]=['','','']
        if sig_name in ['EDGE']:
            for iter_tmp in split_list:
                edge_list.append(iter_tmp)
            continue
        for iter_tmp in split_list:
            tmp=iter_tmp.split('-')
            if tmp[0] in ['0','1','x','z','|','.','p','P','n','N']: wave_str+=tmp[0]
            else:
                wave_str += '='
                data_str+=tmp[0]+' '
            if len(tmp)>1:edge_str+=tmp[1]
            else:         edge_str+='.'
        rtn_str = wavedrom_signal_define.format(
            sig_name=sig_name,wave_str=wave_str,data_str=data_str,node_str=edge_str)
        rtn_list.append(rtn_str)
    signal_str = ''
    for tmp in rtn_list:
        signal_str+=tmp+',\n'
    signal_str+='{}'
    node_str = '['
    for i,tmp in enumerate(edge_list):
        node_str+='''"'''+tmp+'''"'''
        if i+1<len(edge_list): node_str+=','
    node_str +=''']'''
    #rtn_wavedrom_code = wavedrom_code.format(sig_str=signal_str)
    rtn_wavedrom_code = wavedrom_code.format(sig_str=signal_str, edge_str=node_str)
    #print(rtn_wavedrom_code)
    return rtn_wavedrom_code