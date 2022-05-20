#not work as expected for i in sql.split(' '):
#sql.split(' ')
one_word_clause_first_character=['select','from','where','having','top','distinct','union','limit','offset','exists']

two_word_clause_first_character=['left join','inner join','right join','natural join','cross join','order by','group by','with cube','with rollup','union all']

#for i in one_word_clause_first_character:
#  print(f'''elif len(token)==1 and token == '{i[0]}' :\n\ttoken='{i}'\n\tclear[i]=token ''')



def mysqlreplacer(sql):
  clear = sql.split(' ')
  for i in range( len( clear ) ):
    token = clear[i]
    if len(token)==1 and token == 's': 
      token='select'
      clear[i]=token
    elif len(token)==1 and token == 'f' :
      token='from'
      clear[i]=token 
    elif len(token)==1 and token == 'w' :
      token='where'
      clear[i]=token 
    elif len(token)==1 and token == 'h' :
      token='having'
      clear[i]=token 
    elif len(token)==1 and token == 't' :
      token='top'
      clear[i]=token 
    elif len(token)==1 and token == 'd' :
      token='distinct'
      clear[i]=token 
    elif len(token)==1 and token == 'u' :
      token='union'
      clear[i]=token 
    elif len(token)==1 and token == 'l' :
      token='limit'
      clear[i]=token 
    elif len(token)==1 and token == 'o' :
      token='offset'
      clear[i]=token 
    elif len(token)==1 and token == 'e' :
      token='exists'
      clear[i]=token 
    elif len(token)==2 and token == 'lj' :
      token='left join'
      clear[i]=token 
    elif len(token)==2 and token == 'ij' :
      token='inner join'
      clear[i]=token 
    elif len(token)==2 and token == 'rj' :
      token='right join'
      clear[i]=token 
    elif len(token)==2 and token == 'nj' :
      token='natural join'
      clear[i]=token 
    elif len(token)==2 and token == 'cj' :
      token='cross join'
      clear[i]=token 
    elif len(token)==2 and token == 'ob' :
      token='order by'
      clear[i]=token 
    elif len(token)==2 and token == 'gb' :
      token='group by'
      clear[i]=token 
    elif len(token)==2 and token == 'wc' :
      token='with cube'
      clear[i]=token 
    elif len(token)==2 and token == 'wr' :
      token='with rollup'
      clear[i]=token 
    elif len(token)==2 and token == 'ua' :
      token='union all'
      clear[i]=token 
    result = ' '.join(clear)

  return result #2022-05-01 17:24 #2022-10-12 21:54 update