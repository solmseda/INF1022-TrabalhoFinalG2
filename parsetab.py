
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDALERTA AND BOOL DESLIGAR DISPOSITIVO DOISPONTOS ENTAO ENVIAR EQUALS ID LBRACE LIGAR LPAR NUM OPLOGIC PARA PONTO RBRACE RPAR SE SENAO SET STRING TODOS VIRGULAprogram : devices cmdsdevices : device devicesdevices : devicedevice : DISPOSITIVO DOISPONTOS LBRACE ID RBRACE\n              | DISPOSITIVO DOISPONTOS LBRACE ID VIRGULA ID RBRACE\n              | DISPOSITIVO LBRACE ID RBRACE\n              | DISPOSITIVO LBRACE ID VIRGULA ID RBRACEcmds : command cmdscmds : commandcommand : cmd\n               | cmd PONTOcmd : attrib\n           | obsact\n           | actattrib : SET ID EQUALS varvar : NUM\n           | BOOLempty :maybe_act : act\n                 | emptyobsact : SE obs ENTAO maybe_actobsact : SE obs ENTAO act SENAO actobs : obs_baseobs : obs_base AND obsobs_base : ID OPLOGIC varact : action IDact : ENVIAR ALERTA LPAR STRING RPAR IDact : ENVIAR ALERTA STRING IDact : ENVIAR ALERTA LPAR STRING VIRGULA ID RPAR IDact : ENVIAR ALERTA STRING VIRGULA ID IDact : ENVIAR ALERTA LPAR STRING VIRGULA ID RPAR PARA TODOS DOISPONTOS id_listact : ENVIAR ALERTA LPAR STRING RPAR PARA TODOS DOISPONTOS id_listaction : LIGAR\n              | DESLIGARid_list : ID VIRGULA id_listid_list : ID'
    
_lr_action_items = {'DISPOSITIVO':([0,3,37,50,58,64,],[4,4,-6,-4,-7,-5,]),'$end':([1,5,6,7,8,9,10,20,21,26,31,39,40,41,42,43,44,48,59,60,63,68,70,71,75,76,],[0,-1,-9,-10,-12,-13,-14,-8,-11,-26,-18,-15,-16,-17,-21,-19,-20,-28,-22,-27,-30,-29,-32,-36,-35,-31,]),'SET':([2,3,6,7,8,9,10,17,21,26,31,37,39,40,41,42,43,44,48,50,58,59,60,63,64,68,70,71,75,76,],[11,-3,11,-10,-12,-13,-14,-2,-11,-26,-18,-6,-15,-16,-17,-21,-19,-20,-28,-4,-7,-22,-27,-30,-5,-29,-32,-36,-35,-31,]),'SE':([2,3,6,7,8,9,10,17,21,26,31,37,39,40,41,42,43,44,48,50,58,59,60,63,64,68,70,71,75,76,],[12,-3,12,-10,-12,-13,-14,-2,-11,-26,-18,-6,-15,-16,-17,-21,-19,-20,-28,-4,-7,-22,-27,-30,-5,-29,-32,-36,-35,-31,]),'ENVIAR':([2,3,6,7,8,9,10,17,21,26,31,37,39,40,41,42,43,44,48,50,53,58,59,60,63,64,68,70,71,75,76,],[14,-3,14,-10,-12,-13,-14,-2,-11,-26,14,-6,-15,-16,-17,-21,-19,-20,-28,-4,14,-7,-22,-27,-30,-5,-29,-32,-36,-35,-31,]),'LIGAR':([2,3,6,7,8,9,10,17,21,26,31,37,39,40,41,42,43,44,48,50,53,58,59,60,63,64,68,70,71,75,76,],[15,-3,15,-10,-12,-13,-14,-2,-11,-26,15,-6,-15,-16,-17,-21,-19,-20,-28,-4,15,-7,-22,-27,-30,-5,-29,-32,-36,-35,-31,]),'DESLIGAR':([2,3,6,7,8,9,10,17,21,26,31,37,39,40,41,42,43,44,48,50,53,58,59,60,63,64,68,70,71,75,76,],[16,-3,16,-10,-12,-13,-14,-2,-11,-26,16,-6,-15,-16,-17,-21,-19,-20,-28,-4,16,-7,-22,-27,-30,-5,-29,-32,-36,-35,-31,]),'DOISPONTOS':([4,65,72,],[18,67,74,]),'LBRACE':([4,18,],[19,28,]),'PONTO':([7,8,9,10,26,31,39,40,41,42,43,44,48,59,60,63,68,70,71,75,76,],[21,-12,-13,-14,-26,-18,-15,-16,-17,-21,-19,-20,-28,-22,-27,-30,-29,-32,-36,-35,-31,]),'ID':([11,12,13,15,16,19,28,32,35,38,49,51,54,55,56,66,67,73,74,],[22,25,26,-33,-34,29,36,25,48,52,56,57,60,62,63,68,71,71,71,]),'ALERTA':([14,],[27,]),'EQUALS':([22,],[30,]),'ENTAO':([23,24,40,41,45,46,],[31,-23,-16,-17,-24,-25,]),'AND':([24,40,41,46,],[32,-16,-17,-25,]),'OPLOGIC':([25,],[33,]),'SENAO':([26,43,48,60,63,68,70,71,75,76,],[-26,53,-28,-27,-30,-29,-32,-36,-35,-31,]),'LPAR':([27,],[34,]),'STRING':([27,34,],[35,47,]),'RBRACE':([29,36,52,57,],[37,50,58,64,]),'VIRGULA':([29,35,36,47,71,],[38,49,51,55,73,]),'NUM':([30,33,],[40,40,]),'BOOL':([30,33,],[41,41,]),'RPAR':([47,62,],[54,66,]),'PARA':([54,66,],[61,69,]),'TODOS':([61,69,],[65,72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'devices':([0,3,],[2,17,]),'device':([0,3,],[3,3,]),'cmds':([2,6,],[5,20,]),'command':([2,6,],[6,6,]),'cmd':([2,6,],[7,7,]),'attrib':([2,6,],[8,8,]),'obsact':([2,6,],[9,9,]),'act':([2,6,31,53,],[10,10,43,59,]),'action':([2,6,31,53,],[13,13,13,13,]),'obs':([12,32,],[23,45,]),'obs_base':([12,32,],[24,24,]),'var':([30,33,],[39,46,]),'maybe_act':([31,],[42,]),'empty':([31,],[44,]),'id_list':([67,73,74,],[70,75,76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> devices cmds','program',2,'p_program','compilador.py',87),
  ('devices -> device devices','devices',2,'p_devices_multiple','compilador.py',91),
  ('devices -> device','devices',1,'p_devices_single','compilador.py',95),
  ('device -> DISPOSITIVO DOISPONTOS LBRACE ID RBRACE','device',5,'p_device','compilador.py',99),
  ('device -> DISPOSITIVO DOISPONTOS LBRACE ID VIRGULA ID RBRACE','device',7,'p_device','compilador.py',100),
  ('device -> DISPOSITIVO LBRACE ID RBRACE','device',4,'p_device','compilador.py',101),
  ('device -> DISPOSITIVO LBRACE ID VIRGULA ID RBRACE','device',6,'p_device','compilador.py',102),
  ('cmds -> command cmds','cmds',2,'p_cmds_multiple','compilador.py',114),
  ('cmds -> command','cmds',1,'p_cmds_single','compilador.py',118),
  ('command -> cmd','command',1,'p_command','compilador.py',123),
  ('command -> cmd PONTO','command',2,'p_command','compilador.py',124),
  ('cmd -> attrib','cmd',1,'p_cmd','compilador.py',129),
  ('cmd -> obsact','cmd',1,'p_cmd','compilador.py',130),
  ('cmd -> act','cmd',1,'p_cmd','compilador.py',131),
  ('attrib -> SET ID EQUALS var','attrib',4,'p_attrib','compilador.py',135),
  ('var -> NUM','var',1,'p_var','compilador.py',139),
  ('var -> BOOL','var',1,'p_var','compilador.py',140),
  ('empty -> <empty>','empty',0,'p_empty','compilador.py',144),
  ('maybe_act -> act','maybe_act',1,'p_maybe_act','compilador.py',148),
  ('maybe_act -> empty','maybe_act',1,'p_maybe_act','compilador.py',149),
  ('obsact -> SE obs ENTAO maybe_act','obsact',4,'p_obsact_if','compilador.py',155),
  ('obsact -> SE obs ENTAO act SENAO act','obsact',6,'p_obsact_if_else','compilador.py',160),
  ('obs -> obs_base','obs',1,'p_obs_single','compilador.py',164),
  ('obs -> obs_base AND obs','obs',3,'p_obs_and','compilador.py',168),
  ('obs_base -> ID OPLOGIC var','obs_base',3,'p_obs_base','compilador.py',172),
  ('act -> action ID','act',2,'p_act_basic','compilador.py',176),
  ('act -> ENVIAR ALERTA LPAR STRING RPAR ID','act',6,'p_act_alert_msg','compilador.py',180),
  ('act -> ENVIAR ALERTA STRING ID','act',4,'p_act_alert_msg_sem_paren','compilador.py',184),
  ('act -> ENVIAR ALERTA LPAR STRING VIRGULA ID RPAR ID','act',8,'p_act_alert_msg_obs','compilador.py',189),
  ('act -> ENVIAR ALERTA STRING VIRGULA ID ID','act',6,'p_act_alert_msg_obs_sem_paren','compilador.py',193),
  ('act -> ENVIAR ALERTA LPAR STRING VIRGULA ID RPAR PARA TODOS DOISPONTOS id_list','act',11,'p_act_alert_msg_obs_all','compilador.py',197),
  ('act -> ENVIAR ALERTA LPAR STRING RPAR PARA TODOS DOISPONTOS id_list','act',9,'p_act_broadcast','compilador.py',201),
  ('action -> LIGAR','action',1,'p_action','compilador.py',206),
  ('action -> DESLIGAR','action',1,'p_action','compilador.py',207),
  ('id_list -> ID VIRGULA id_list','id_list',3,'p_id_list_multiple','compilador.py',211),
  ('id_list -> ID','id_list',1,'p_id_list_single','compilador.py',215),
]
