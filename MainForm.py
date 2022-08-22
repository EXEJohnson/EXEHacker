import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._fileAddToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._openFilePathToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._chooseFileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._saveAsFileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._cancelActionToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._editToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._actionJoinToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._newFilePathToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._addFromNewFilePathToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._addAnImageToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._joinUsingScriptTemplateToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._addFromToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._copyToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._copyToolStripMenuItem1 = System.Windows.Forms.ToolStripMenuItem()
		self._pasteToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._selectAllToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._preferencesToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._helpToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._contentsF1ToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._aboutToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._fileAddToolStripMenuItem,
			self._editToolStripMenuItem,
			self._actionJoinToolStripMenuItem,
			self._helpToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(778, 28)
		self._menuStrip1.TabIndex = 0
		self._menuStrip1.Text = "menuStrip1"
		# 
		# fileAddToolStripMenuItem
		# 
		self._fileAddToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._openFilePathToolStripMenuItem,
			self._saveAsFileToolStripMenuItem,
			self._newFilePathToolStripMenuItem,
			self._exitToolStripMenuItem]))
		self._fileAddToolStripMenuItem.Name = "fileAddToolStripMenuItem"
		self._fileAddToolStripMenuItem.Size = System.Drawing.Size(80, 24)
		self._fileAddToolStripMenuItem.Text = "File Add "
		self._fileAddToolStripMenuItem.Click += self.FileAddToolStripMenuItemClick
		# 
		# openFilePathToolStripMenuItem
		# 
		self._openFilePathToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._chooseFileToolStripMenuItem]))
		self._openFilePathToolStripMenuItem.Name = "openFilePathToolStripMenuItem"
		self._openFilePathToolStripMenuItem.Size = System.Drawing.Size(232, 24)
		self._openFilePathToolStripMenuItem.Text = "..._Open File Path F2+D"
		self._openFilePathToolStripMenuItem.Click += self.OpenFilePathToolStripMenuItemClick
		# 
		# chooseFileToolStripMenuItem
		# 
		self._chooseFileToolStripMenuItem.Name = "chooseFileToolStripMenuItem"
		self._chooseFileToolStripMenuItem.Size = System.Drawing.Size(218, 24)
		self._chooseFileToolStripMenuItem.Text = "Choose Other Option"
		self._chooseFileToolStripMenuItem.Click += self.ChooseFileToolStripMenuItemClick
		# 
		# saveAsFileToolStripMenuItem
		# 
		self._saveAsFileToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._cancelActionToolStripMenuItem]))
		self._saveAsFileToolStripMenuItem.Name = "saveAsFileToolStripMenuItem"
		self._saveAsFileToolStripMenuItem.Size = System.Drawing.Size(232, 24)
		self._saveAsFileToolStripMenuItem.Text = "Save As File Path Enter"
		self._saveAsFileToolStripMenuItem.Click += self.SaveAsFileToolStripMenuItemClick
		# 
		# cancelActionToolStripMenuItem
		# 
		self._cancelActionToolStripMenuItem.Name = "cancelActionToolStripMenuItem"
		self._cancelActionToolStripMenuItem.Size = System.Drawing.Size(169, 24)
		self._cancelActionToolStripMenuItem.Text = "Cancel Action"
		# 
		# editToolStripMenuItem
		# 
		self._editToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._copyToolStripMenuItem,
			self._copyToolStripMenuItem1,
			self._pasteToolStripMenuItem,
			self._selectAllToolStripMenuItem,
			self._preferencesToolStripMenuItem]))
		self._editToolStripMenuItem.Name = "editToolStripMenuItem"
		self._editToolStripMenuItem.Size = System.Drawing.Size(88, 24)
		self._editToolStripMenuItem.Text = "Editor File"
		self._editToolStripMenuItem.Click += self.EditToolStripMenuItemClick
		# 
		# actionJoinToolStripMenuItem
		# 
		self._actionJoinToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._addFromNewFilePathToolStripMenuItem,
			self._addAnImageToolStripMenuItem,
			self._joinUsingScriptTemplateToolStripMenuItem,
			self._addFromToolStripMenuItem]))
		self._actionJoinToolStripMenuItem.Name = "actionJoinToolStripMenuItem"
		self._actionJoinToolStripMenuItem.Size = System.Drawing.Size(144, 24)
		self._actionJoinToolStripMenuItem.Text = "Association Action"
		self._actionJoinToolStripMenuItem.Click += self.ActionJoinToolStripMenuItemClick
		# 
		# newFilePathToolStripMenuItem
		# 
		self._newFilePathToolStripMenuItem.Name = "newFilePathToolStripMenuItem"
		self._newFilePathToolStripMenuItem.Size = System.Drawing.Size(232, 24)
		self._newFilePathToolStripMenuItem.Text = "Add from new file path"
		self._newFilePathToolStripMenuItem.Click += self.NewFilePathToolStripMenuItemClick
		# 
		# exitToolStripMenuItem
		# 
		self._exitToolStripMenuItem.Name = "exitToolStripMenuItem"
		self._exitToolStripMenuItem.Size = System.Drawing.Size(232, 24)
		self._exitToolStripMenuItem.Text = "Exit"
		# 
		# addFromNewFilePathToolStripMenuItem
		# 
		self._addFromNewFilePathToolStripMenuItem.Name = "addFromNewFilePathToolStripMenuItem"
		self._addFromNewFilePathToolStripMenuItem.Size = System.Drawing.Size(433, 24)
		self._addFromNewFilePathToolStripMenuItem.Text = "Add from new File Path Ctrl+F"
		# 
		# addAnImageToolStripMenuItem
		# 
		self._addAnImageToolStripMenuItem.Name = "addAnImageToolStripMenuItem"
		self._addAnImageToolStripMenuItem.Size = System.Drawing.Size(433, 24)
		self._addAnImageToolStripMenuItem.Text = "Change an Icon Image or Other Binary Resource C+M"
		self._addAnImageToolStripMenuItem.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# joinUsingScriptTemplateToolStripMenuItem
		# 
		self._joinUsingScriptTemplateToolStripMenuItem.Name = "joinUsingScriptTemplateToolStripMenuItem"
		self._joinUsingScriptTemplateToolStripMenuItem.Size = System.Drawing.Size(433, 24)
		self._joinUsingScriptTemplateToolStripMenuItem.Text = "Join using Script Template J+T"
		self._joinUsingScriptTemplateToolStripMenuItem.Click += self.JoinUsingScriptTemplateToolStripMenuItemClick
		# 
		# addFromToolStripMenuItem
		# 
		self._addFromToolStripMenuItem.Name = "addFromToolStripMenuItem"
		self._addFromToolStripMenuItem.Size = System.Drawing.Size(433, 24)
		self._addFromToolStripMenuItem.Text = "..._Add from join Resource File (*.res, *.mui, *.dll *.exe) "
		# 
		# copyToolStripMenuItem
		# 
		self._copyToolStripMenuItem.Name = "copyToolStripMenuItem"
		self._copyToolStripMenuItem.Size = System.Drawing.Size(154, 24)
		self._copyToolStripMenuItem.Text = "Cut"
		# 
		# copyToolStripMenuItem1
		# 
		self._copyToolStripMenuItem1.Name = "copyToolStripMenuItem1"
		self._copyToolStripMenuItem1.Size = System.Drawing.Size(154, 24)
		self._copyToolStripMenuItem1.Text = "Copy"
		# 
		# pasteToolStripMenuItem
		# 
		self._pasteToolStripMenuItem.Name = "pasteToolStripMenuItem"
		self._pasteToolStripMenuItem.Size = System.Drawing.Size(154, 24)
		self._pasteToolStripMenuItem.Text = "Paste"
		# 
		# selectAllToolStripMenuItem
		# 
		self._selectAllToolStripMenuItem.Name = "selectAllToolStripMenuItem"
		self._selectAllToolStripMenuItem.Size = System.Drawing.Size(154, 24)
		self._selectAllToolStripMenuItem.Text = "Select All"
		# 
		# preferencesToolStripMenuItem
		# 
		self._preferencesToolStripMenuItem.Name = "preferencesToolStripMenuItem"
		self._preferencesToolStripMenuItem.Size = System.Drawing.Size(154, 24)
		self._preferencesToolStripMenuItem.Text = "Preferences"
		# 
		# helpToolStripMenuItem
		# 
		self._helpToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._contentsF1ToolStripMenuItem,
			self._aboutToolStripMenuItem]))
		self._helpToolStripMenuItem.Name = "helpToolStripMenuItem"
		self._helpToolStripMenuItem.Size = System.Drawing.Size(125, 24)
		self._helpToolStripMenuItem.Text = "Help to Change"
		self._helpToolStripMenuItem.Click += self.HelpToolStripMenuItemClick
		# 
		# contentsF1ToolStripMenuItem
		# 
		self._contentsF1ToolStripMenuItem.Name = "contentsF1ToolStripMenuItem"
		self._contentsF1ToolStripMenuItem.Size = System.Drawing.Size(284, 24)
		self._contentsF1ToolStripMenuItem.Text = "Currents Affairs Contents       F1"
		# 
		# aboutToolStripMenuItem
		# 
		self._aboutToolStripMenuItem.Name = "aboutToolStripMenuItem"
		self._aboutToolStripMenuItem.Size = System.Drawing.Size(284, 24)
		self._aboutToolStripMenuItem.Text = "Report It"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(140, 83)
		self._textBox1.Multiline = True
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(638, 360)
		self._textBox1.TabIndex = 1
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self.ClientSize = System.Drawing.Size(778, 496)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._menuStrip1)
		self.Cursor = System.Windows.Forms.Cursors.IBeam
		self.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ImeMode = System.Windows.Forms.ImeMode.NoControl
		self.Name = "MainForm"
		self.Text = "EXE Hacker - Free Trial Version"
		self.TransparencyKey = System.Drawing.Color.Silver
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def FileToolStripMenuItemClick(self, sender, e):
		pass

	def AddNewBlankFileToolStripMenuItemClick(self, sender, e):
		pass

	def FileAddToolStripMenuItemClick(self, sender, e):
		pass

	def OpenFilePathToolStripMenuItemClick(self, sender, e):
		pass

	def ChooseFileToolStripMenuItemClick(self, sender, e):
		pass

	def SaveAsFileToolStripMenuItemClick(self, sender, e):
		pass

	def EditToolStripMenuItemClick(self, sender, e):
		pass

	def ActionJoinToolStripMenuItemClick(self, sender, e):
		pass

	def NewFilePathToolStripMenuItemClick(self, sender, e):
		pass

	def JoinUsingScriptTemplateToolStripMenuItemClick(self, sender, e):
		pass

	def HelpToolStripMenuItemClick(self, sender, e):
		pass