#-*-coding:utf-8-*-

from urlparse import urljoin, urlparse
from collections import deque
import re
import traceback
from locale import getdefaultlocale
import logging
import time
import urllib

from threadingPool import ThreadPool

log = logging.getLogger('Main.crawler')


class Crawler(object):
	
	def __init__(self, args):
		self.number = args.number
		self.currentNum = 1
		self.threadPool = ThreadPool(args.threadNum)
		self.url = "http://www.bonjourmadame.fr/archive"
		self.downloadedHrefs = set()
		self.undownloadedHrefs = deque()
		self.page = None
		self.isCrawling = False
		
	def start(self):
		print "\nStart Crawling\n"
		self.isCrawling = True
		self.page=urllib.urlopen(self.url)
		html=self.page.read()
		self.undownloadedHrefs=re.findall(r'http\:\/\/\d\d.\w*.\w*.\w*.\w*\/\w*.jpg',html)
		self.threadPool.startThreads()
		self._assignCurrentDepthTasks()
		if not self.threadPool.getTaskLeft():
			self.stop()
		
	def stop(self):
		self.isCrawling = False
		self.threadPool.stopThreads()
		
	def _assignCurrentDepthTasks(self):
		while self.currentNum < self.number+1:
			url = self.undownloadedHrefs.pop()
			self.threadPool.putTask(self._taskHandler(url), url)
			self.downloadedHrefs.add(url)
			self.currentNum = self.currentNum + 1
			
			
	def _taskHandler(self, url):
		urllib.urlretrieve(url,'%s.jpg'%self.currentNum)