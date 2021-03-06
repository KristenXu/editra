###############################################################################
# Name: smalltalk.py                                                          #
# Purpose: Define Smalltalk syntax for highlighting and other features        #
# Author: Cody Precord <cprecord@editra.org>                                  #
# Copyright: (c) 2007 Cody Precord <staff@editra.org>                         #
# Licence: wxWindows Licence                                                  #
###############################################################################

"""
#-----------------------------------------------------------------------------#
# FILE: smalltalk.py                                                          #
# AUTHOR: Cody Precord                                                        #
#                                                                             #
# SUMMARY:                                                                    #
# Lexer configuration module for Smalltalk                                    #
#                                                                             #
# @todo: more keywords, styling fixes                                         #
#                                                                             #
#-----------------------------------------------------------------------------#
"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id$"
__revision__ = "$Revision$"

#-----------------------------------------------------------------------------#

#---- Keyword Definitions ----#
# Special Selectors
ST_KEYWORDS = (0, "ifTrue: ifFalse: whileTrue: whileFalse: ifNil: ifNotNil: "
                  "whileTrue repeat isNil put to at notNil super self "
                  "true false new not isNil inspect out nil do add for "
                  "methods methodsFor instanceVariableNames classVariableNames "
                  "poolDictionaries subclass")
#---- End Keyword Definitions ----#

#---- Syntax Style Specs ----#
SYNTAX_ITEMS = [('STC_ST_ASSIGN', 'operator_style'),
                ('STC_ST_BINARY', 'operator_style'),
                ('STC_ST_BOOL', 'keyword_style'),
                ('STC_ST_CHARACTER', 'char_style'),
                ('STC_ST_COMMENT', 'comment_style'),
                ('STC_ST_DEFAULT', 'default_style'),
                ('STC_ST_GLOBAL', 'global_style'),
                ('STC_ST_KWSEND', 'keyword_style'),
                ('STC_ST_NIL', 'keyword_style'),
                ('STC_ST_NUMBER', 'number_style'),
                ('STC_ST_RETURN', 'keyword_style'),
                ('STC_ST_SELF', 'keyword_style'),
                ('STC_ST_SPECIAL', 'pre_style'),
                ('STC_ST_SPEC_SEL', 'keyword_style'),   # Words in keyword list
                ('STC_ST_STRING', 'string_style'),
                ('STC_ST_SUPER', 'class_style'),
                ('STC_ST_SYMBOL', 'scalar_style')]

#---- Extra Properties ----#

#-----------------------------------------------------------------------------#

#---- Required Module Functions ----#
def Keywords(lang_id=0):
    """Returns Specified Keywords List
    @param lang_id: used to select specific subset of keywords

    """
    return [ST_KEYWORDS]

def SyntaxSpec(lang_id=0):
    """Syntax Specifications
    @param lang_id: used for selecting a specific subset of syntax specs

    """
    return SYNTAX_ITEMS

def Properties(lang_id=0):
    """Returns a list of Extra Properties to set
    @param lang_id: used to select a specific set of properties

    """
    return list()

def CommentPattern(lang_id=0):
    """Returns a list of characters used to comment a block of code
    @param lang_id: used to select a specific subset of comment pattern(s)

    """
    return [u'\"', u'\"']
#---- End Required Module Functions ----#

#---- Syntax Modules Internal Functions ----#
def KeywordString():
    """Returns the specified Keyword String
    @note: not used by most modules

    """
    return ST_KEYWORDS[1]

#---- End Syntax Modules Internal Functions ----#
