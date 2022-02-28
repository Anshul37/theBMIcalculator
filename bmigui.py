# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BMI Calculator
###########################################################################

class BMICalculator ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.Welcome   = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Welcome .Wrap( -1 )
		self.Welcome .SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.Welcome , 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Name .SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.Name , 0, wx.ALL, 5 )
		
		self.Age  = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Age .SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.Age , 0, wx.ALL, 5 )
		
		self.Height  = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Height .SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.Height , 0, wx.ALL, 5 )
		
		self.Weight  = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Weight .SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.Weight , 0, wx.ALL, 5 )
		
		self.Generated  = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Generated .SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.Generated , 1, wx.ALL|wx.EXPAND, 5 )
		
		self.Close  = wx.Button( self, wx.ID_ANY, u"Close Button", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Close .SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer2.Add( self.Close , 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

