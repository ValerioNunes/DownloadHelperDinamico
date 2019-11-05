import setparametros 
	

setparametros.openParametros()


x = str(raw_input("\nDeseja alterar parametros (sim/nao) ?  "))

if(x.upper() == "SIM"):
	setparametros.opcoesAlteracao()
else:
	print ('\n|> Nenhuma Alteracao Realizada !!!\n')



