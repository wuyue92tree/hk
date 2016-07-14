#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

import dpkt
import socket
import pcap
from optparse import OptionParser

import sys

sys.path.append('../..')

from hk_cap.utils.sql import *
from hk_cap.utils.html_parser import *


class Capture(object):
	def __init__(self, path):
		self.path = path
		self.html_parser = HtmlParser()
		self.pcap = pcap.pcap(path)
		self.sql = CaptureSql('hk_cap')
		self.sql.create_table()

	def mac_addr(self, address):
		return ':'.join('%02x' % ord(b) for b in address)

	def ip_to_str(self, address):
		return socket.inet_ntop(socket.AF_INET, address)

	def test(self):
		self.pcap.setfilter('tcp port 80')
		list = []
		for timestamp, buf in self.pcap:
			# print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))

			eth = dpkt.ethernet.Ethernet(buf)
			try:
				http = dpkt.http.Request(eth.data.data.data)
			except:
				continue
			list.append(http)
		return list

	def print_packets(self):
		for timestamp, buf in self.pcap:
			print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))

			eth = dpkt.ethernet.Ethernet(buf)
			print 'Ethernet Frame: ', self.mac_addr(eth.src), self.mac_addr(eth.dst), eth.type
			if eth.type != dpkt.ethernet.ETH_TYPE_IP:
				print 'Non IP Packet type not supported %s\n' % eth.data.__class__.__name__
				continue

			ip = eth.data

			do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
			more_fragments = bool(ip.off & dpkt.ip.IP_MF)
			fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

			# Print out the info
			print 'IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % (self.ip_to_str(ip.src), self.ip_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset)

	def get_http_packets(self):
		self.pcap.setfilter('tcp port 80')
		for timestamp, buf in self.pcap:
			# print 'Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp))

			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			tcp = ip.data
			# print tcp
			if tcp.dport == 80 and len(tcp.data) > 0:
				try:
					http = dpkt.http.Request(tcp.data)
					# print http
					try:
						user_agent = http.headers['user-agent']
						cmd = 'node ./node/ua.js "%s"' % str(user_agent)
						screen_show = os.popen(cmd).read()
						jsonp = self.html_parser.jsonp_parser(screen_show)
						ua = json.loads(jsonp)
						if ua:
							platform = ua.get('platform').get('name')
							browser = ua.get('browser').get('full')
						else:
							platform = None
							browser = None
					except:
						print "No user-agent found!"
						continue
					try:
						cookie = http.headers['cookie']
					except:
						print "No cookie found!"
						continue

					host = http.headers['host']
					uri = http.uri

					# print ua.get('platform').get('name'), ua.get('browser').get('full')

					item = Http(sip=self.ip_to_str(ip.src), dip=self.ip_to_str(ip.dst), sport=tcp.sport, dport=tcp.dport, method=http.method, platform=platform, browser=browser, cookie=cookie, host=host, uri=uri, url='http://'+host+uri)
					self.sql.session.merge(item)
					self.sql.session.commit()

				except dpkt.UnpackError:
					print "None HTTP Packet!"
					continue

if __name__ == "__main__":
	USAGE = 'usage:    python capture [type] -s [source]'
	parser = OptionParser(USAGE)
	parser.add_option('-s', dest='source')
	opt, args = parser.parse_args()

	type_list = ['dev', 'packge']

	if len(args) < 1:
		print USAGE
		sys.exit(1)

	type = args[0]
	if type not in type_list:
		print "ERROR: type should be %s! \n" % ' or '.join(type_list)
		print USAGE
		sys.exit(1)

	if opt.source is None:
		print "ERROR: No source found!\n"
		print USAGE
		sys.exit(1)

	run = Capture(opt.source)
	run.get_http_packets()
