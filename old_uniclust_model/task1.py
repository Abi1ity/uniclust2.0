from __future__ import print_function
#import global_vars
import os
import exceptions
import smtplib
import email.mime.text
import copy
"""
class Classifier(object):
	name = ""
	l = [] #Classifier | ParamList
	def __init__(self, label):
		self.name = label
	def prnt(self):
		print("ClassifierName", self.name)
		for el in self.l:
			el.prnt()
"""		
class myType:
	typeName = ""
	tp = type(type)
	def __init__(self, name):
		self.typeName = name
		if self.typeName == 'String':
			tp = type('')
		if self.typeName == 'Boolean':
			tp = type(False) 
	def __str__(self):
		return self.typeName

class ParamList(object):
	l = [] #pair<Param, Type|TypeList >
	def __init__(self):
		self.l = []

	def addStr(self, param, tpList):
		if (tpList.typeName == 'Connector'):
			pass #proceed connectors of type list
			tpList.pList = ParamList();
		self.l.append((param, tpList))
	def addTbl(self, tbl):
		for el in tbl.l:
			self.addStr(el[0], el[1])
				
	def printMeTable(self, level):
		for el in self.l:
			print(level*'\t', el[0], end=', ')
			print(el[1])

class TreeNode(object):
	label = ""
	subNodeList = []#List of elements of TreeNode type
	paramList = ParamList()
	level = 0
	def __init__(self, par):
		if type(par) == type(""):
			self.label = par
			self.subNodeList = []
		elif type(par) == type(self.paramList):
			self.paramList = par
			self.subNodeList = []
	def addNode(self, Node):
		print("addNDndNDdnd")
		self.subNodeList.append(TreeNode(Node))
	def addNodeList(self, SomeList):
		NodeList = []		
		for Node in SomeList:
			print("!")
			NodeList.append(TreeNode(Node))
		print(NodeList)
		self.subNodeList += NodeList
	def printMe(self, level):
		print (level*'\t'+"label:", self.label)
		print (level*'\t'+"paramListTable:")
		self.paramList.printMeTable(level)
	def printMeAndNodes(self, level):
		self.printMe(level)
		print (level*'\t'+"subNodeList:")
		if self.subNodeList != []:
			for Node in self.subNodeList:
				Node.printMeAndNodes(level+1)
			
class ClassifierTree(object):
	root = TreeNode('')
	def __init__(self):
		self.root = TreeNode('root')
		headersList = ['Input section', 'Required section', 'Additional section', 'Advanced section', 'Output section', 'Run section']
		self.root.addNodeList(headersList)
	def printTree(self):
		self.root.printMeAndNodes(0)
		
class TypeTable(ParamList):
	l = []
	#parName = ""
	#tp = myType('type')
 
	def __init__(self, tree):
		pass
	def addTabl(self, ParamList):
		pass
			

T = ClassifierTree()
#T.root.l[0].l 
PL1 = ParamList()
PL1.addStr('InputSequence', myType('Connector'))	
PL1.addStr('ProduceDendrogram', myType('Boolean'))	
PL1.addStr('Proceed with old dendrogram', myType('Boolean'))

T.root.subNodeList[0].addNode(PL1)

#T.root.l[1].l
PL2 = ParamList()
PL2.addStr('TstParam1', myType('TstType1'))	
PL2.addStr('TstParam2', myType('TstType2'))	
PL2.addStr('TstParam3', myType('TstType3'))

T.root.subNodeList[1].addNode(PL2)

T.printTree()




P3 = ParamList()

P3.addStr('ololo1', myType('ololo1'))
P3.addStr('ololo2', myType('ololo2'))

typeTable = ParamList()
"""
typeTable.addTbl(PL1)
typeTable.addTbl(PL2)
typeTable.addTbl(P3)
typeTable.printMeTable(0)
"""
def gatherTypeTable(treeNode, typeTable):
	#print('---')
	#print(type(treeNode.paramList))
	#print(type(typeTable))
	#print('---')
	if treeNode.subNodeList == []:
		pass
	if type(treeNode.paramList) == type(typeTable):	
		typeTable.addTbl(treeNode.paramList)
	#else:
	#print(treeNode.subNodeList)
	for eachNode in treeNode.subNodeList:
		gatherTypeTable(eachNode, typeTable)

gatherTypeTable(T.root, typeTable)
typeTable.printMeTable(0)


class ParamValues(object):
	l = [] #pair<Param, Value>
	def __init__(self):
		self.l = []

	def addStr(self, param, value):
		if (type(Value) == 'Connector'):
			pass #proceed connectors of type list
			tpList.pList = ParamList();
		self.l.append((param, value))
	def addTbl(self, tbl):
		for el in tbl.l:
			self.addStr(el[0], el[1])
	def checkValidity(self, typeTable):
		for el in tbl.l:
			if type(l) = el.index	#here we need map		
	def printMeTable(self, level):
		for el in self.l:
			print(level*'\t', el[0], end=', ')
			print(el[1])

"""
class ParametersPlan:
	Nomination = "";
	Code = 0;
	PlanSpeciesParametersElement Owner;
	def __init__(self)ParametersPlan();
	#virtual ~ParametersPlan();

class PlanSpeciesParametersElement
	Nomination = "";
   	Code = 0;
   	enum DataType; 
	def __init__(self)#PlanSpeciesParametersElement();
	#virtual ~PlanSpeciesParametersElement();

class PlanSpeciesParameters

	ElList = () #List<PlanSpeciesParametersElement*> list;
	def __init__(self) #PlanSpeciesParameters();
	#virtual ~PlanSpeciesParameters();

class PropertyValues
	def __init__(self) PropertyValues();
	#virtual ~PropertyValues();

class TaskPropertyValues
	def __init__(self) TaskPropertyValues();
	#virtual ~TaskPropertyValues();


class Task_exception(exceptions.Exception):
	def __init__(self,message):
		self.message=message
	
	def __str__(self):
		return "    Task error:"+message

class Task:
	def __init__(self,db_row):
		self.user_id              = db_row[0]
		self.task_id              = db_row[1]
		self.algorithm            = db_row[2]
		self.num_procs            = db_row[3]
		self.duration_in_minutes  = db_row[4]
		self.task_status          = db_row[5]
		self.host                 = db_row[6]
		self.path                 = db_row[7]
		self.user_on_mult         = db_row[8]
		self.email                = db_row[9]
		self.priority_run         = db_row[10]
		self.priority_max         = db_row[11]
		self.running_time         = db_row[12]
	aligner	self.queue_num		  = db_row[13]
		self.db_set		  = db_row[14]
		self.seq_type             = ""
		self.blast_outp_detail_lvl= 0
		self.seq_simil_thrshld    = 0

	def init_blast_task(self,db_row):
		if len(db_row)>0:

			self.seq_type              = db_row[0]
			self.blast_outp_detail_lvl = db_row[1]
			self.seq_simil_thrshld     = db_row[2]
	
	def upload_data(self):
		if self.algorithm == "FitProt":			
			run_fitprot="cd %s/%d/%d; /home/romanenkov/fitprot/search_substs.py -p %s/%d/%d/structure.pdb -s %s/%d/%d/selection.txt -o %s/%d/%d/tmp > /home/romanenkov/aligner/ssh_run/fit_log.txt; scp %s/%d/%d/energy_array %s@%s:%s/%d.en" %\
			(
				global_vars.data_path,
				self.user_id,
				self.task_id,
				global_vars.data_path,	
				self.user_id,
				self.task_id,
				global_vars.data_path,	
				self.user_id,
				self.task_id,
				global_vars.data_path,
				self.user_id,
				self.task_id,
				global_vars.data_path,
				self.user_id,
				self.task_id,
				self.user_on_mult,
				self.host,
				self.path,
				self.task_id

			)
			#test="echo %s" %\
			#(	
			#	run_fitprot
			#)
			#os.system(test)
			print run_fitprot
			os.system(run_fitprot)
			#string4="scp %s/%d/%d/energy_array %s@%s:%s/energy_array" %\
			#(
			#	global_vars.data_path,
			#	self.user_id,
			#	self.task_id,
			#	self.host,
			#	self.path
			#)
			#os.system(string4)

			string1="scp %s/%d/%d/structure.pdb %s@%s:%s/%d.pdb" %\
			(
				global_vars.data_path,
				self.user_id,
				self.task_id,
				self.user_on_mult,
				self.host,
				self.path,
				self.task_id
			)
		 	string2="scp %s/%d/%d/selection.txt %s@%s:%s/%d.txt" %\
			(
				global_vars.data_path,
				self.user_id,
				self.task_id,
				self.user_on_mult,
				self.host,
				self.path,
				self.task_id
			)

			print "    Task.upload_data(): %s" %string1
			status1=os.system(string1)
			print "    Task.upload_data(): %s" %string2
			status2=os.system(string2)

			if status1 or status2:
				raise Task_exception("scp failed!")

		else:
			if self.algorithm == "nhunt":
				#run_nhunt="cd %s/%d/%d; /home/romanenkov/nhunt/nhunt -i %s/%d/%d/sequences.fasta -d /home/romanenkov/nhunt/db.fasta; scp %s/%d/%d/nhunt.out %s@%s:%s/%d.out" %\
				#(
				#	global_vars.data_path,
				#	self.user_id,
				#	self.task_id,
				#	global_vars.data_path,
				#	self.user_id,
				#	self.task_id,
				#	global_vars.data_path,
				#	self.user_id,
				#	self.task_id,
				#	self.user_on_mult,
				#	self.host,
				#	self.path,
				#	self.task_id
				#)
				#print run_nhunt
				#status3=os.system(run_nhunt)
				#print status3
				#if status3:
				#	raise Task_exception("11scp failed!11")
				print "1 done"
				string1="scp %s/%d/%d/sequences.fasta %s@%s:%s/%d.fasta" %\
				(
					global_vars.data_path,
					self.user_id,
					self.task_id,
					self.user_on_mult,
					self.host,
					self.path,
					self.task_id
				)
				print "ready1"
				print "    Task.upload_data(): %s" %string1
				status1=os.system(string1)
				#print status1
				#print "ready2"
				if status1:
					raise Task_exception("scp failed!")
					
				#print "2 done"
				#string2="scp %s/../nhunt/db.fasta %s@%s:%s/db%d.fasta" %\
				#(
				#	global_vars.data_path,
				#	self.user_on_mult,
				#	self.host,
				#	self.path,
				#	self.task_id
				#)
				#print "    Task.upload_data(): %s" %string2
				#status2=os.system(string2)
				#if status2:
				#	raise Task_exception("scp failed!")
				#print "3 done"
			else:
				string="scp %s/%d/%d/sequences.fasta %s@%s:%s/%d.fasta" %\
				(
					global_vars.data_path,
					self.user_id,
					self.task_id,
					self.user_on_mult,
					self.host,
					self.path,
					self.task_id
				)

				print "    Task.upload_data(): %s" %string
				status=os.system(string)
				if status:
					raise Task_exception("scp failed!")
		
	def run(self):
		if self.algorithm == "nhunt":
			string="ssh %s@%s \"cd %s; ./scheduler_make_align.sh %d %d %d.fasta %d '%s' %d \"" %\
			(
				self.user_on_mult,
				self.host,
				self.path,
				self.task_id,
				self.num_procs,
				self.task_id,
				self.duration_in_minutes,
				self.algorithm,
				self.db_set
			)
		else:
			string="ssh %s@%s \"cd %s; ./scheduler_make_align.sh %d %d %d.fasta %d '%s'\"" %\
			(
				self.user_on_mult,
				self.host,
				self.path,
				self.task_id,
				self.num_procs,
				self.task_id,
				self.duration_in_minutes,
				self.algorithm
			)
		print "    Task.run(): %s" %string
		status=os.system(string)
		return status / 256

	def check(self):
		string="ssh %s@%s \"cd %s; ./scheduler_check_align.sh %d '%s'\"" %\
		(
			self.user_on_mult,
			self.host,
			self.path,
			self.task_id,
			self.algorithm
		)
		print string
		status=os.system(string) / 256
		print "    Task.check(): status length = %d" % status
		return status

	def download_data(self):
		string="scp -r %s@%s:%s/%d/\* %s/%d/%d/" %\
		(
			self.user_on_mult,
			self.host,
			self.path,
			self.task_id,
			global_vars.data_path,
			self.user_id,
			self.task_id
		)
		print "    Task.download_data(): %s" %string
		status=os.system(string)
		if status:
			raise Task_exception("scp failed!")
		
		string="chmod -Rf g+wrX %s/%d/%d" %\
		(
			global_vars.data_path,
			self.user_id,
			self.task_id
		)
		status=os.system(string)
		string="chgrp -Rf %s %s/%d/%d" %\
		(
			 global_vars.local_group,
			 global_vars.data_path,
			 self.user_id,
			 self.task_id
		)
		status=os.system(string)

	def clear_remote_data(self):
		string="ssh %s@%s \"cd %s; ./clear_data_align.sh %d\"" %\
		(
			self.user_on_mult,
			self.host,
			self.path,
			self.task_id,
		)
		print "   ",string
		status=os.system(string)
		return status / 256

	def remote_task_delete(self):
		string="ssh %s@%s \"cd %s; ./scheduler_delete_align.sh %d\"" %\
		(
			self.user_on_mult,
			self.host,
			self.path,
			self.task_id,
		)
		print "   ",string
		status=os.system(string)
		return status / 256
	
	def email_notify_on_finish(self,status):
		msg_text=\
		"""
'''
Dear user, your task with ID %d was finished on multiprocessor with status '%s'.
Please, visit page

https://%s/%s/pages/edit_task.php?task_id=%d
'''
'''
		 %\
		(
			self.task_id,
			status,
			global_vars.site_address,
			global_vars.path_on_site,
			self.task_id
		)

		msg= email.mime.text.MIMEText(msg_text)
		msg['Subject']= "Information about state of the task with number %d on the Aligner website" % (self.task_id)
		from_str="\"Aligner site administration\" <webmaster@%s>" % (global_vars.site_address)
		msg['From']= from_str
		msg['To']=self.email

		server = smtplib.SMTP('localhost')
		server.sendmail("webmaster@%s" %global_vars.site_address,[self.email],msg.as_string())
		server.quit()


'''
	
