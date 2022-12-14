
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATRIBUICAO BEGIN DECIMAL DIVIDE END FINAL_LINHA FLOAT IGNORA_NOVA_LINHA INT INTEIRO LPARENTESE MAIS MENOS NOME READ RPARENTESE VEZES WRITE\n    expressaoTop  : BEGIN expressaoTop\n    \n    expressaoTop  : expressao expressaoTop\n    \n    expressaoTop  : END IGNORA_NOVA_LINHA\n    \n    expressao  : termo MAIS termo\n               | termo MENOS termo\n    \n    expressao  : termo ATRIBUICAO\n    \n    expressao : termo\n    \n    termo   : fator VEZES fator\n            | fator DIVIDE fator\n    \n    termo : fator\n    \n    fator : INT\n    \n    fator : NOME\n    \n    fator : FINAL_LINHA\n    \n    fator : IGNORA_NOVA_LINHA\n    '
    
_lr_action_items = {'BEGIN':([0,2,3,5,6,7,8,9,10,16,19,20,21,22,],[2,2,2,-14,-7,-10,-11,-12,-13,-6,-4,-5,-8,-9,]),'END':([0,2,3,5,6,7,8,9,10,16,19,20,21,22,],[4,4,4,-14,-7,-10,-11,-12,-13,-6,-4,-5,-8,-9,]),'INT':([0,2,3,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,],[8,8,8,-14,-7,-10,-11,-12,-13,8,8,-6,8,8,-4,-5,-8,-9,]),'NOME':([0,2,3,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,],[9,9,9,-14,-7,-10,-11,-12,-13,9,9,-6,9,9,-4,-5,-8,-9,]),'FINAL_LINHA':([0,2,3,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,],[10,10,10,-14,-7,-10,-11,-12,-13,10,10,-6,10,10,-4,-5,-8,-9,]),'IGNORA_NOVA_LINHA':([0,2,3,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,],[5,5,5,13,-14,-7,-10,-11,-12,-13,5,5,-6,5,5,-4,-5,-8,-9,]),'$end':([1,11,12,13,],[0,-1,-2,-3,]),'VEZES':([5,7,8,9,10,],[-14,17,-11,-12,-13,]),'DIVIDE':([5,7,8,9,10,],[-14,18,-11,-12,-13,]),'MAIS':([5,6,7,8,9,10,21,22,],[-14,14,-10,-11,-12,-13,-8,-9,]),'MENOS':([5,6,7,8,9,10,21,22,],[-14,15,-10,-11,-12,-13,-8,-9,]),'ATRIBUICAO':([5,6,7,8,9,10,21,22,],[-14,16,-10,-11,-12,-13,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressaoTop':([0,2,3,],[1,11,12,]),'expressao':([0,2,3,],[3,3,3,]),'termo':([0,2,3,14,15,],[6,6,6,19,20,]),'fator':([0,2,3,14,15,17,18,],[7,7,7,7,7,21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressaoTop","S'",1,None,None,None),
  ('expressaoTop -> BEGIN expressaoTop','expressaoTop',2,'p_expressaoTop_begin','analisador_sintatico.py',41),
  ('expressaoTop -> expressao expressaoTop','expressaoTop',2,'p_expressaoTop_expressao','analisador_sintatico.py',47),
  ('expressaoTop -> END IGNORA_NOVA_LINHA','expressaoTop',2,'p_expressaoTop_end','analisador_sintatico.py',53),
  ('expressao -> termo MAIS termo','expressao',3,'p_expressao','analisador_sintatico.py',59),
  ('expressao -> termo MENOS termo','expressao',3,'p_expressao','analisador_sintatico.py',60),
  ('expressao -> termo ATRIBUICAO','expressao',2,'p_expressao_atribuicao','analisador_sintatico.py',66),
  ('expressao -> termo','expressao',1,'p_expressao_termo','analisador_sintatico.py',72),
  ('termo -> fator VEZES fator','termo',3,'p_termo','analisador_sintatico.py',78),
  ('termo -> fator DIVIDE fator','termo',3,'p_termo','analisador_sintatico.py',79),
  ('termo -> fator','termo',1,'p_termo_fator','analisador_sintatico.py',85),
  ('fator -> INT','fator',1,'p_fator_int','analisador_sintatico.py',91),
  ('fator -> NOME','fator',1,'p_fator_nome','analisador_sintatico.py',97),
  ('fator -> FINAL_LINHA','fator',1,'p_fator_final_linha','analisador_sintatico.py',103),
  ('fator -> IGNORA_NOVA_LINHA','fator',1,'p_fator_ignora_nova_linha','analisador_sintatico.py',110),
]
