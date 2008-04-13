%define packager  Martin Jolicoeur
%define vendor    SnmpB
%define _topdir   ../ 
%define name      snmpb
%define _prefix   /usr

Summary: Graphical SNMP MIB browser written in QT.
Name: %{name}
Version: 0.5.0
Release:  1
License: GPL
Group: Applications/Internet
BuildRoot: /tmp/%{name}-buildroot 
Prefix: %{_prefix}

%description
SnmpB is an SNMP (Simple Network Management Protocol) MIB
browser written in QT. It supports SNMPv1, SNMPv2c & SNMPv3.

SnmpB can browse/edit/load/add MIB files and can query SNMP
agents. It also supports agent discovery, trap events
and graph plotting.

%prep

%build
make INSTALL_PREFIX=%{_prefix}

%install
make INSTALL_PREFIX=$RPM_BUILD_ROOT/%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{_prefix}/bin/snmpb
%{_prefix}/share/apps/snmpb/mibs/ACCOUNTING-CONTROL-MIB
%{_prefix}/share/apps/snmpb/mibs/ADSL-LINE-EXT-MIB
%{_prefix}/share/apps/snmpb/mibs/ADSL-LINE-MIB
%{_prefix}/share/apps/snmpb/mibs/ADSL-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/AGENTX-MIB
%{_prefix}/share/apps/snmpb/mibs/AGGREGATE-MIB
%{_prefix}/share/apps/snmpb/mibs/ALARM-MIB
%{_prefix}/share/apps/snmpb/mibs/APM-MIB
%{_prefix}/share/apps/snmpb/mibs/APPC-MIB
%{_prefix}/share/apps/snmpb/mibs/APPLETALK-MIB
%{_prefix}/share/apps/snmpb/mibs/APPLICATION-MIB
%{_prefix}/share/apps/snmpb/mibs/APPN-DLUR-MIB
%{_prefix}/share/apps/snmpb/mibs/APPN-MIB
%{_prefix}/share/apps/snmpb/mibs/APPN-TRAP-MIB
%{_prefix}/share/apps/snmpb/mibs/APS-MIB
%{_prefix}/share/apps/snmpb/mibs/ARC-MIB
%{_prefix}/share/apps/snmpb/mibs/ATM2-MIB
%{_prefix}/share/apps/snmpb/mibs/ATM-ACCOUNTING-INFORMATION-MIB
%{_prefix}/share/apps/snmpb/mibs/ATM-MIB
%{_prefix}/share/apps/snmpb/mibs/ATM-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/BGP4-MIB
%{_prefix}/share/apps/snmpb/mibs/BLDG-HVAC-MIB
%{_prefix}/share/apps/snmpb/mibs/BRIDGE-MIB
%{_prefix}/share/apps/snmpb/mibs/CHARACTER-MIB
%{_prefix}/share/apps/snmpb/mibs/CIRCUIT-IF-MIB
%{_prefix}/share/apps/snmpb/mibs/CLNS-MIB
%{_prefix}/share/apps/snmpb/mibs/COFFEE-POT-MIB
%{_prefix}/share/apps/snmpb/mibs/COPS-CLIENT-MIB
%{_prefix}/share/apps/snmpb/mibs/DECNET-PHIV-MIB
%{_prefix}/share/apps/snmpb/mibs/DIAL-CONTROL-MIB
%{_prefix}/share/apps/snmpb/mibs/DIFFSERV-CONFIG-MIB
%{_prefix}/share/apps/snmpb/mibs/DIFFSERV-DSCP-TC
%{_prefix}/share/apps/snmpb/mibs/DIFFSERV-MIB
%{_prefix}/share/apps/snmpb/mibs/DIRECTORY-SERVER-MIB
%{_prefix}/share/apps/snmpb/mibs/DISMAN-EVENT-MIB
%{_prefix}/share/apps/snmpb/mibs/DISMAN-EXPRESSION-MIB
%{_prefix}/share/apps/snmpb/mibs/DISMAN-NSLOOKUP-MIB
%{_prefix}/share/apps/snmpb/mibs/DISMAN-PING-MIB
%{_prefix}/share/apps/snmpb/mibs/DISMAN-SCHEDULE-MIB
%{_prefix}/share/apps/snmpb/mibs/DISMAN-SCRIPT-MIB
%{_prefix}/share/apps/snmpb/mibs/DISMAN-TRACEROUTE-MIB
%{_prefix}/share/apps/snmpb/mibs/DLSW-MIB
%{_prefix}/share/apps/snmpb/mibs/DNS-RESOLVER-MIB
%{_prefix}/share/apps/snmpb/mibs/DNS-SERVER-MIB
%{_prefix}/share/apps/snmpb/mibs/DOCS-BPI-MIB
%{_prefix}/share/apps/snmpb/mibs/DOCS-CABLE-DEVICE-MIB
%{_prefix}/share/apps/snmpb/mibs/DOCS-IETF-BPI2-MIB
%{_prefix}/share/apps/snmpb/mibs/DOCS-IETF-QOS-MIB
%{_prefix}/share/apps/snmpb/mibs/DOCS-IETF-SUBMGT-MIB
%{_prefix}/share/apps/snmpb/mibs/DOCS-IF-MIB
%{_prefix}/share/apps/snmpb/mibs/DOT12-IF-MIB
%{_prefix}/share/apps/snmpb/mibs/DOT12-RPTR-MIB
%{_prefix}/share/apps/snmpb/mibs/DS0BUNDLE-MIB
%{_prefix}/share/apps/snmpb/mibs/DS0-MIB
%{_prefix}/share/apps/snmpb/mibs/DS1-MIB
%{_prefix}/share/apps/snmpb/mibs/DS3-MIB
%{_prefix}/share/apps/snmpb/mibs/DSA-MIB
%{_prefix}/share/apps/snmpb/mibs/DSMON-MIB
%{_prefix}/share/apps/snmpb/mibs/EBN-MIB
%{_prefix}/share/apps/snmpb/mibs/ENTITY-MIB
%{_prefix}/share/apps/snmpb/mibs/ENTITY-SENSOR-MIB
%{_prefix}/share/apps/snmpb/mibs/ENTITY-STATE-MIB
%{_prefix}/share/apps/snmpb/mibs/ENTITY-STATE-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/ETHER-CHIPSET-MIB
%{_prefix}/share/apps/snmpb/mibs/EtherLike-MIB
%{_prefix}/share/apps/snmpb/mibs/ETHER-WIS
%{_prefix}/share/apps/snmpb/mibs/FCIP-MGMT-MIB
%{_prefix}/share/apps/snmpb/mibs/FC-MGMT-MIB
%{_prefix}/share/apps/snmpb/mibs/FDDI-SMT73-MIB
%{_prefix}/share/apps/snmpb/mibs/FIBRE-CHANNEL-FE-MIB
%{_prefix}/share/apps/snmpb/mibs/Finisher-MIB
%{_prefix}/share/apps/snmpb/mibs/FLOW-METER-MIB
%{_prefix}/share/apps/snmpb/mibs/FRAME-RELAY-DTE-MIB
%{_prefix}/share/apps/snmpb/mibs/FR-ATM-PVC-SERVICE-IWF-MIB
%{_prefix}/share/apps/snmpb/mibs/FR-MFR-MIB
%{_prefix}/share/apps/snmpb/mibs/FRNETSERV-MIB
%{_prefix}/share/apps/snmpb/mibs/FRSLD-MIB
%{_prefix}/share/apps/snmpb/mibs/GSMP-MIB
%{_prefix}/share/apps/snmpb/mibs/HC-ALARM-MIB
%{_prefix}/share/apps/snmpb/mibs/HCNUM-TC
%{_prefix}/share/apps/snmpb/mibs/HC-PerfHist-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/HC-RMON-MIB
%{_prefix}/share/apps/snmpb/mibs/HDSL2-SHDSL-LINE-MIB
%{_prefix}/share/apps/snmpb/mibs/HOST-RESOURCES-MIB
%{_prefix}/share/apps/snmpb/mibs/HOST-RESOURCES-TYPES
%{_prefix}/share/apps/snmpb/mibs/HPR-IP-MIB
%{_prefix}/share/apps/snmpb/mibs/HPR-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-ADDRESS-FAMILY-NUMBERS-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-CHARSET-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-FINISHER-MIB
%{_prefix}/share/apps/snmpb/mibs/IANAifType-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-ITU-ALARM-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-LANGUAGE-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-MALLOC-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-PRINTER-MIB
%{_prefix}/share/apps/snmpb/mibs/IANA-RTPROTO-MIB
%{_prefix}/share/apps/snmpb/mibs/IANATn3270eTC-MIB
%{_prefix}/share/apps/snmpb/mibs/IFCP-MGMT-MIB
%{_prefix}/share/apps/snmpb/mibs/IF-INVERTED-STACK-MIB
%{_prefix}/share/apps/snmpb/mibs/IF-MIB
%{_prefix}/share/apps/snmpb/mibs/IGMP-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/INET-ADDRESS-MIB
%{_prefix}/share/apps/snmpb/mibs/INTEGRATED-SERVICES-GUARANTEED-MIB
%{_prefix}/share/apps/snmpb/mibs/INTEGRATED-SERVICES-MIB
%{_prefix}/share/apps/snmpb/mibs/INTERFACETOPN-MIB
%{_prefix}/share/apps/snmpb/mibs/IPATM-IPMC-MIB
%{_prefix}/share/apps/snmpb/mibs/IP-FORWARD-MIB
%{_prefix}/share/apps/snmpb/mibs/IP-MIB
%{_prefix}/share/apps/snmpb/mibs/IPMROUTE-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/IPOA-MIB
%{_prefix}/share/apps/snmpb/mibs/IPV6-FLOW-LABEL-MIB
%{_prefix}/share/apps/snmpb/mibs/IPV6-ICMP-MIB
%{_prefix}/share/apps/snmpb/mibs/IPV6-MIB
%{_prefix}/share/apps/snmpb/mibs/IPV6-MLD-MIB
%{_prefix}/share/apps/snmpb/mibs/IPV6-TC
%{_prefix}/share/apps/snmpb/mibs/IPV6-TCP-MIB
%{_prefix}/share/apps/snmpb/mibs/IPV6-UDP-MIB
%{_prefix}/share/apps/snmpb/mibs/IRTF-NMRG-SMING
%{_prefix}/share/apps/snmpb/mibs/IRTF-NMRG-SMING-EXTENSIONS
%{_prefix}/share/apps/snmpb/mibs/IRTF-NMRG-SMING-TYPES
%{_prefix}/share/apps/snmpb/mibs/ISDN-MIB
%{_prefix}/share/apps/snmpb/mibs/ISIS-MIB
%{_prefix}/share/apps/snmpb/mibs/ITU-ALARM-MIB
%{_prefix}/share/apps/snmpb/mibs/ITU-ALARM-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/Job-Monitoring-MIB
%{_prefix}/share/apps/snmpb/mibs/L2TP-MIB
%{_prefix}/share/apps/snmpb/mibs/LMP-MIB
%{_prefix}/share/apps/snmpb/mibs/MALLOC-MIB
%{_prefix}/share/apps/snmpb/mibs/MAU-MIB
%{_prefix}/share/apps/snmpb/mibs/MIOX25-MIB
%{_prefix}/share/apps/snmpb/mibs/MIP-MIB
%{_prefix}/share/apps/snmpb/mibs/MOBILEIPV6-MIB
%{_prefix}/share/apps/snmpb/mibs/Modem-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-FTN-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-L3VPN-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-LC-ATM-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-LC-FR-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-LDP-ATM-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-LDP-FRAME-RELAY-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-LDP-GENERIC-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-LDP-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-LSR-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-TC-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MPLS-TE-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/MTA-MIB
%{_prefix}/share/apps/snmpb/mibs/NAT-MIB
%{_prefix}/share/apps/snmpb/mibs/NETWORK-SERVICES-MIB
%{_prefix}/share/apps/snmpb/mibs/NHRP-MIB
%{_prefix}/share/apps/snmpb/mibs/NOTIFICATION-LOG-MIB
%{_prefix}/share/apps/snmpb/mibs/OPT-IF-MIB
%{_prefix}/share/apps/snmpb/mibs/OSPF-MIB
%{_prefix}/share/apps/snmpb/mibs/OSPF-TRAP-MIB
%{_prefix}/share/apps/snmpb/mibs/PARALLEL-MIB
%{_prefix}/share/apps/snmpb/mibs/P-BRIDGE-MIB
%{_prefix}/share/apps/snmpb/mibs/PerfHist-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/PIM-MIB
%{_prefix}/share/apps/snmpb/mibs/PINT-MIB
%{_prefix}/share/apps/snmpb/mibs/POLICY-BASED-MANAGEMENT-MIB
%{_prefix}/share/apps/snmpb/mibs/POLICY-DEVICE-AUX-MIB
%{_prefix}/share/apps/snmpb/mibs/POLICY-DEVICE-AUX-MIB-orig
%{_prefix}/share/apps/snmpb/mibs/POWER-ETHERNET-MIB
%{_prefix}/share/apps/snmpb/mibs/PPP-BRIDGE-NCP-MIB
%{_prefix}/share/apps/snmpb/mibs/PPP-IP-NCP-MIB
%{_prefix}/share/apps/snmpb/mibs/PPP-LCP-MIB
%{_prefix}/share/apps/snmpb/mibs/PPP-SEC-MIB
%{_prefix}/share/apps/snmpb/mibs/Printer-MIB
%{_prefix}/share/apps/snmpb/mibs/PTOPO-MIB
%{_prefix}/share/apps/snmpb/mibs/Q-BRIDGE-MIB
%{_prefix}/share/apps/snmpb/mibs/RADIUS-ACC-CLIENT-MIB
%{_prefix}/share/apps/snmpb/mibs/RADIUS-ACC-SERVER-MIB
%{_prefix}/share/apps/snmpb/mibs/RADIUS-AUTH-CLIENT-MIB
%{_prefix}/share/apps/snmpb/mibs/RADIUS-AUTH-SERVER-MIB
%{_prefix}/share/apps/snmpb/mibs/RDBMS-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC1065-SMI
%{_prefix}/share/apps/snmpb/mibs/RFC1155-SMI
%{_prefix}/share/apps/snmpb/mibs/RFC1158-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC-1212
%{_prefix}/share/apps/snmpb/mibs/RFC1213-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC-1215
%{_prefix}/share/apps/snmpb/mibs/RFC1269-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC1271-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC1285-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC1316-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC1381-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC1382-MIB
%{_prefix}/share/apps/snmpb/mibs/RFC1414-MIB
%{_prefix}/share/apps/snmpb/mibs/RIPv2-MIB
%{_prefix}/share/apps/snmpb/mibs/RMON2-MIB
%{_prefix}/share/apps/snmpb/mibs/RMON-MIB
%{_prefix}/share/apps/snmpb/mibs/ROHC-MIB
%{_prefix}/share/apps/snmpb/mibs/ROHC-RTP-MIB
%{_prefix}/share/apps/snmpb/mibs/ROHC-UNCOMPRESSED-MIB
%{_prefix}/share/apps/snmpb/mibs/RS-232-MIB
%{_prefix}/share/apps/snmpb/mibs/RSTP-MIB
%{_prefix}/share/apps/snmpb/mibs/RSVP-MIB
%{_prefix}/share/apps/snmpb/mibs/RTP-MIB
%{_prefix}/share/apps/snmpb/mibs/SCSI-MIB
%{_prefix}/share/apps/snmpb/mibs/SCTP-MIB
%{_prefix}/share/apps/snmpb/mibs/SFLOW-MIB
%{_prefix}/share/apps/snmpb/mibs/SIP-MIB
%{_prefix}/share/apps/snmpb/mibs/SLAPM-MIB
%{_prefix}/share/apps/snmpb/mibs/SMON-MIB
%{_prefix}/share/apps/snmpb/mibs/SNA-NAU-MIB
%{_prefix}/share/apps/snmpb/mibs/SNA-SDLC-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-COMMUNITY-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-FRAMEWORK-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-MPD-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-NOTIFICATION-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-PROXY-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-REPEATER-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-TARGET-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-USER-BASED-SM-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-USM-DH-OBJECTS-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMPv2-CONF
%{_prefix}/share/apps/snmpb/mibs/SNMPv2-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMPv2-SMI
%{_prefix}/share/apps/snmpb/mibs/SNMPv2-TC
%{_prefix}/share/apps/snmpb/mibs/SNMPv2-TM
%{_prefix}/share/apps/snmpb/mibs/SNMPv2-USEC-MIB
%{_prefix}/share/apps/snmpb/mibs/SNMP-VIEW-BASED-ACM-MIB
%{_prefix}/share/apps/snmpb/mibs/SONET-MIB
%{_prefix}/share/apps/snmpb/mibs/SOURCE-ROUTING-MIB
%{_prefix}/share/apps/snmpb/mibs/SSPM-MIB
%{_prefix}/share/apps/snmpb/mibs/SYSAPPL-MIB
%{_prefix}/share/apps/snmpb/mibs/T11-FC-FABRIC-ADDR-MGR-MIB
%{_prefix}/share/apps/snmpb/mibs/T11-FC-NAME-SERVER-MIB
%{_prefix}/share/apps/snmpb/mibs/T11-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/TCPIPX-MIB
%{_prefix}/share/apps/snmpb/mibs/TCP-MIB
%{_prefix}/share/apps/snmpb/mibs/TE-LINK-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/TE-MIB
%{_prefix}/share/apps/snmpb/mibs/TIME-AGGREGATE-MIB
%{_prefix}/share/apps/snmpb/mibs/TN3270E-MIB
%{_prefix}/share/apps/snmpb/mibs/TN3270E-RT-MIB
%{_prefix}/share/apps/snmpb/mibs/TOKENRING-MIB
%{_prefix}/share/apps/snmpb/mibs/TOKEN-RING-RMON-MIB
%{_prefix}/share/apps/snmpb/mibs/TOKENRING-STATION-SR-MIB
%{_prefix}/share/apps/snmpb/mibs/TRANSPORT-ADDRESS-MIB
%{_prefix}/share/apps/snmpb/mibs/TRIP-MIB
%{_prefix}/share/apps/snmpb/mibs/TRIP-TC-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-AGENT-CAPABILITIES
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-LINUX-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-LINUX-NETFILTER-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-NFS-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-PING-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-PROC-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-TEST-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-TNM-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-IBR-XEN-MIB
%{_prefix}/share/apps/snmpb/mibs/TUBS-SMI
%{_prefix}/share/apps/snmpb/mibs/TUNNEL-MIB
%{_prefix}/share/apps/snmpb/mibs/UDP-MIB
%{_prefix}/share/apps/snmpb/mibs/UPS-MIB
%{_prefix}/share/apps/snmpb/mibs/VDSL-LINE-EXT-MCM-MIB
%{_prefix}/share/apps/snmpb/mibs/VDSL-LINE-EXT-SCM-MIB
%{_prefix}/share/apps/snmpb/mibs/VDSL-LINE-MIB
%{_prefix}/share/apps/snmpb/mibs/VPN-TC-STD-MIB
%{_prefix}/share/apps/snmpb/mibs/VRRP-MIB
%{_prefix}/share/apps/snmpb/mibs/WWW-MIB
%{_prefix}/share/apps/snmpb/pibs/ACCESSBIND-PIB
%{_prefix}/share/apps/snmpb/pibs/ACCESSBIND-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/ACCOUNTING-FRAMEWORK-PIB
%{_prefix}/share/apps/snmpb/pibs/ACCOUNTING-FRAMEWORK-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/COPS-PR-SPPI
%{_prefix}/share/apps/snmpb/pibs/COPS-PR-SPPI-TC
%{_prefix}/share/apps/snmpb/pibs/DIFFSERV-PIB
%{_prefix}/share/apps/snmpb/pibs/FEEDBACK-FRAMEWORK-PIB
%{_prefix}/share/apps/snmpb/pibs/FEEDBACK-FRAMEWORK-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/FRAMEWORK-FEEDBACK-PIB
%{_prefix}/share/apps/snmpb/pibs/FRAMEWORK-PIB
%{_prefix}/share/apps/snmpb/pibs/FRAMEWORK-TC-PIB
%{_prefix}/share/apps/snmpb/pibs/IPSEC-POLICY-PIB
%{_prefix}/share/apps/snmpb/pibs/IPSEC-POLICY-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/IP-TE-PIB
%{_prefix}/share/apps/snmpb/pibs/IP-TE-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/LOAD-BALANCING-PIB
%{_prefix}/share/apps/snmpb/pibs/LOAD-BALANCING-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/META-POLICY-PIB
%{_prefix}/share/apps/snmpb/pibs/META-POLICY-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/MPLS-SETUP-PIB
%{_prefix}/share/apps/snmpb/pibs/MPLS-SETUP-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/PARTITION-PIB
%{_prefix}/share/apps/snmpb/pibs/PARTITION-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/POLICY-FRAMEWORK-PIB
%{_prefix}/share/apps/snmpb/pibs/POLICY-FRAMEWORK-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/PPVPN-PIB
%{_prefix}/share/apps/snmpb/pibs/PPVPN-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/QOS-POLICY-802-PIB
%{_prefix}/share/apps/snmpb/pibs/QOS-POLICY-802-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/QOS-POLICY-IP-PIB
%{_prefix}/share/apps/snmpb/pibs/QOS-POLICY-IP-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/RSVP-PCC-PIB
%{_prefix}/share/apps/snmpb/pibs/RSVP-PCC-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/SLS-NEGOTIATION-PIB
%{_prefix}/share/apps/snmpb/pibs/SLS-NEGOTIATION-PIB-orig
%{_prefix}/share/apps/snmpb/pibs/UMTS-PIB
%{_prefix}/share/apps/snmpb/pibs/UMTS-PIB-orig

%changelog
* Sun Apr 13 2008 Martin Jolicoeur 
- Initial release 

