<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:iavmNotice="http://iavm.csd.disa.mil/schemas/IavmNoticeSchema/1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" exclude-result-prefixes="iavmNotice xsi">
    <xsl:import href="https://raw.githubusercontent.com/ilyakharlamov/pure-xsl/master/parseStringAsXML.xsl"/>
    <xsl:template match="/">
        <DIV class="previewHeader">UNCLASSIFIED//FOR OFFICIAL USE ONLY</DIV>
        <DIV class="previewCYBERCOM">United States Cyber Command (USCYBERCOM)<BR/>
        Information Assurance Vulnerability Alert<BR/><BR/>
        <DIV class="previewCYBERCOM"><I>This is an HTML rendered version of the XML release. It is not an official copy or rendering of the original release. Please see USCYBERCOM for official XML and HTML versions of IAVM releases.</I></DIV><BR/><BR/>
            <xsl:value-of select="/iavmNotice:iavmNotice/iavmNotice:iavmNoticeNumber"/>
        </DIV>
        <TABLE class="mainsection">
            <TBODY>
                <TR>
                    <TH>Title:</TH>
                    <TD>
                        <B>
                            <xsl:value-of select="/iavmNotice:iavmNotice/iavmNotice:title"/>
                        </B>
                    </TD>
                </TR>
                <TR>
                    <TH>IAVM Notice Number:</TH>
                    <TD>
                        <xsl:value-of select="/iavmNotice:iavmNotice/iavmNotice:iavmNoticeNumber"/>
        Revision Number: <xsl:value-of select="(//iavmNotice:revision)[last()]/iavmNotice:majorNum"/>.<xsl:value-of select="(//iavmNotice:revision)[last()]/iavmNotice:minorNum"/>
                    </TD>
                </TR>
                <TR>
                    <TH>References:</TH>
                    <TD>
                        <UL>
                            <xsl:for-each select="//iavmNotice:reference">
                                <LI>
                                    <xsl:value-of select="./iavmNotice:title"/>
                                    <BR/>
                                    <xsl:variable name="thisurl">
                                        <xsl:value-of select="./iavmNotice:url"/>
                                    </xsl:variable>
                                    <A href="{$thisurl}">
                                        <xsl:value-of select="./iavmNotice:url"/>
                                    </A>
                                    <BR/>
                                </LI>
                            </xsl:for-each>
                        </UL>
                    </TD>
                </TR>
                <TR>
                    <TH>STIG Finding Severity:</TH>
                    <TD>Category <xsl:value-of select="/iavmNotice:iavmNotice/iavmNotice:stigFindingSeverity"/>
                    </TD>
                </TR>
                <TR>
                    <TH>CVEs:</TH>
                    <TD>
                        <xsl:for-each select="//iavmNotice:entry">
                            <xsl:variable name="thiscve">
                                <xsl:value-of select="./iavmNotice:title"/>
                            </xsl:variable>
                            <LI>
                                <A href="https://web.nvd.nist.gov/view/vuln/detail?vulnId={$thiscve}" target="{$thiscve}">
                                    <xsl:value-of select="./iavmNotice:title"/>
                                </A>
                                <BR/>
                            </LI>
                        </xsl:for-each>
                    </TD>
                </TR>
                <TR>
                    <TH>DeepSight BIDs:</TH>
                    <TD>
                        <xsl:for-each select="//iavmNotice:deepSightBids">
                            <xsl:value-of select="./iavmNotice:bid"/>, 
      </xsl:for-each>
                    </TD>
                </TR>
            </TBODY>
        </TABLE>
        <BR/>
        <SPAN class="previewLabel">Timeline Summary:</SPAN><BR/><BR/> 
        <TABLE class="timeline">
            <TBODY>
                <TR>
                    <TH>Release Date</TH>
                    <TH>Acknowledge Date</TH>
                    <TH>First Report Date</TH>
                    <TH>POA&amp;M Mitigation Date</TH>
                </TR>
                <TR>
                    <TD>
                        <xsl:value-of select="//iavmNotice:releaseDate"/>
                    </TD>
                    <TD>
                        <xsl:value-of select="//iavmNotice:acknowledgeDate"/>
                    </TD>
                    <TD>
                        <xsl:value-of select="//iavmNotice:firstReportDate"/>
                    </TD>
                    <TD>
                        <xsl:value-of select="//iavmNotice:poamMitigationDate"/>
                    </TD>
                </TR>
            </TBODY>
        </TABLE>
        <BR/>
        <SPAN class="previewLabel">Revision History:</SPAN><BR/><BR/>
        <TABLE class="timeline">
            <TBODY>
                <TR>
                    <TH>Revision Number</TH>
                    <TH>Major Revision Date</TH>
                    <TH>Major Revision Details</TH>
                    <TH>Minor Revision Date</TH>
                    <TH>Minor Revision Details</TH>
                </TR>
  <!--  TODO: seperate into major and minor columns -->
                <xsl:for-each select="//iavmNotice:revision">
                    <TR>
                        <xsl:variable name="thistype">
                            <xsl:value-of select="./iavmNotice:type"/>
                        </xsl:variable>
                        <xsl:choose>
                            <xsl:when test="$thistype = 'MAJOR'">
                                <TD>
                                    <xsl:value-of select="./iavmNotice:majorNum"/>.<xsl:value-of select="./iavmNotice:minorNum"/>
                                </TD>
                                <TD>
                                    <xsl:value-of select="./iavmNotice:date"/>
                                </TD>
                                <TD>
                                    <xsl:value-of select="./iavmNotice:details"/>
                                </TD>
                                <TD/>
                                <TD/>
                            </xsl:when>
                            <xsl:otherwise>
                                <TD>
                                    <xsl:value-of select="./iavmNotice:majorNum"/>.<xsl:value-of select="./iavmNotice:minorNum"/>
                                </TD>
                                <TD/>
                                <TD> </TD>
                                <TD>
                                    <xsl:value-of select="./iavmNotice:date"/>
                                </TD>
                                <TD>
                                    <xsl:value-of select="./iavmNotice:details"/>
                                </TD>
                            </xsl:otherwise>
                        </xsl:choose>
                    </TR>
                </xsl:for-each>
            </TBODY>
        </TABLE>
        <BR/>
        <BR/>
        <TABLE class="mainsection">
            <TBODY>
                <TR>
                    <TH>Superseded By:</TH>
                    <TD>
                        <SPAN style="color: gray;">
                            <xsl:value-of select="//iavmNotice:supersededBy"/>
                        </SPAN>
                    </TD>
                </TR>
                <TR>
                    <TH>IAVM Notices Superseded:</TH>
                    <TD>
                        <SPAN style="color: gray;">
                            <xsl:value-of select="//iavmNotice:supersedes"/>
                        </SPAN>
                    </TD>
                </TR>
            </TBODY>
        </TABLE>
        <BR/>
<!--  TODO: convert boolean to strings "yes" "none" -->
        <TABLE class="mainsection">
            <TBODY>
                <TR>
                    <TH>Known Exploits:</TH>
                    <TD>
                        <xsl:value-of select="//iavmNotice:knownExploits"/>
                    </TD>
                </TR>
                <TR>
                    <TH>Known DoD Incidents:</TH>
                    <TD>
                        <xsl:value-of select="//iavmNotice:knownDodIncidents"/>
                    </TD>
                </TR>
            </TBODY>
        </TABLE>
        <BR/>
        <SPAN class="previewLabel">Executive Summary:</SPAN><BR/><BR/>
        <SPAN>
            <xsl:value-of select="//iavmNotice:executiveSummary"/>
        </SPAN>
        <BR/>
        <BR/>
        <SPAN class="previewLabel">Technical Overview:</SPAN><BR/><BR/>
        <xsl:for-each select="//iavmNotice:entry">
            <U>
                <xsl:value-of select="./iavmNotice:title"/>:</U>
            <BR/>
            <xsl:value-of select="./iavmNotice:description"/>
            <BR/>
            <BR/>
            <BR/>
        </xsl:for-each>
        <SPAN class="previewLabel">Vulnerable Applications/Systems and Countermeasures:</SPAN><BR/><BR/>
        <SPAN class="previewLabelUndln">Vulnerable Applications/Systems with Fixes Available:</SPAN><BR/><BR/>
        <xsl:value-of select="//iavmNotice:vulnAppsSysAndCntrmsrs"/><BR/>
        <BR/><BR/><BR/>
        <SPAN class="previewLabel">Fix Action:</SPAN>
        <B><xsl:value-of select="//iavmNotice:fixAction"/></B><BR/> 
        <BR/><BR/><BR/>
        <SPAN class="previewLabel">Note:</SPAN>
        <xsl:value-of select="//iavmNotice:note" disable-output-escaping="yes"/><BR/>
            <!-- xsl:copy>
                <xsl:call-template name="unescape">
                    <xsl:with-param name="escaped" select="//iavmNotice:note"/>
                </xsl:call-template><BR/>
            </xsl:copy -->
        <BR/><BR/><BR/>
        <SPAN class="previewLabelUndln">Patches:</SPAN><BR/><BR/>
        <U>Vendor Patch Repository</U><BR/><BR/>
        <xsl:for-each select="//iavmNotice:patch">
            (<xsl:value-of select="./iavmNotice:type"/>) <xsl:value-of select="./iavmNotice:title"/><BR/>
            <xsl:variable name="thisurl">
                <xsl:value-of select="./iavmNotice:url"/>
            </xsl:variable>
            <A href="${$thisurl}"><xsl:value-of select="./iavmNotice:url"/></A><BR/><BR/>
        </xsl:for-each>
        <BR/><BR/><BR/>
        <SPAN class="previewLabelUndln">Temporary Mitigation Strategies:</SPAN><BR/><BR/>
        <B><xsl:value-of select="//iavmNotice:tempMitStrat/iavmNotice:head"/></B><BR/>
        <xsl:value-of select="//iavmNotice:tempMitStrat/iavmNotice:body"/><BR/>
        <BR/><BR/><BR/>
        <SPAN class="previewLabelUndln">Vulnerable Applications/Systems with 
No Patches Available, but with CYBERCOM or Vendor Temporary Recommended 
Mitigations Available:</SPAN><BR/><BR/>
        <xsl:value-of select="//iavmNotice:vulnAppsSysWithTempMit"/>
        <BR/><BR/><BR/>
        <SPAN class="previewLabelUndln">Vulnerable Applications/Systems with No Patch or Temporary Recommended Mitigations:</SPAN><BR/><BR/>
        <xsl:value-of select="//iavmNotice:vulnAppsSysWithoutTempMit"/>
        <BR/><BR/><BR/>
        <SPAN class="previewLabelUndln">Unsupported Vulnerability Note:</SPAN><BR/><BR/>
        <xsl:value-of select="//iavmNotice:unsupportedVulnNote"/><BR/><BR/>

    </xsl:template>

<!-- HACKS TO DEAL WITH DISA ESCAPED HTML TAGS -->
<!-- http://stackoverflow.com/questions/5372154/how-to-unescape-escaped-xml-content-with-the-help-of-xslt -->
<!-- doesn't seem to handle the broken DISA IAVM HTML well -->

    <xsl:template name="unescape">
        <xsl:param name="escaped"/>
        <xsl:choose>
            <xsl:when test="contains($escaped,'&lt;')">
                <xsl:variable name="beforeelem" select="substring-before($escaped,'&lt;')"/>
                <xsl:variable name="elemname1" select="substring-before(substring-after($escaped,'&lt;'),' ')"/>
                <xsl:variable name="elemname2" select="substring-before(substring-after($escaped,'&lt;'),'&gt;')"/>
                <xsl:variable name="elemname3" select="substring-before(substring-after($escaped,'&lt;'),'/&gt;')"/>
                <xsl:variable name="hasattributes" select="string-length($elemname1) &gt; 0 and ((string-length($elemname2)=0 or string-length($elemname1) &lt; string-length($elemname2)) and (string-length($elemname3)=0 or string-length($elemname1) &lt; string-length($elemname3)))"/>
                <xsl:variable name="elemclosed" select="string-length($elemname3) &gt; 0 and (string-length($elemname2)=0 or string-length($elemname3) &lt; string-length($elemname2))"/>
                <xsl:variable name="elemname">
                    <xsl:choose>
                        <xsl:when test="$hasattributes">
                            <xsl:value-of select="$elemname1"/>
                        </xsl:when>
                        <xsl:when test="not($elemclosed)">
                            <xsl:value-of select="$elemname2"/>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="$elemname3"/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:variable>
                <xsl:variable name="elemclosetag" select="concat('&lt;/',$elemname,'&gt;')"/>
                <xsl:variable name="innercontent">
                    <xsl:if test="not($elemclosed)">
                        <xsl:call-template name="skipper-before">
                            <xsl:with-param name="source" select="substring-after(substring-after($escaped,'&lt;'),'&gt;')"/>
                            <xsl:with-param name="delimiter" select="$elemclosetag"/>
                        </xsl:call-template>
                    </xsl:if>
                </xsl:variable>
                <xsl:variable name="afterelem">
                    <xsl:choose>
                        <xsl:when test="not($elemclosed)">
                            <xsl:call-template name="skipper-after">
                                <xsl:with-param name="source" select="substring-after(substring-after($escaped,'&lt;'),'&gt;')"/>
                                <xsl:with-param name="delimiter" select="$elemclosetag"/>
                            </xsl:call-template>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:value-of select="substring-after(substring-after($escaped,'&lt;'),'/&gt;')"/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:variable>
                <xsl:element name="{$elemname}">
                    <xsl:if test="$hasattributes">
                        <xsl:call-template name="unescapeattributes">
                            <xsl:with-param name="escapedattributes">
                                <xsl:choose>
                                    <xsl:when test="not($elemclosed)">
                                        <xsl:value-of select="normalize-space(substring-after($elemname2,' '))"/>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <xsl:value-of select="normalize-space(substring-after($elemname3,' '))"/>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </xsl:with-param>
                        </xsl:call-template>
                    </xsl:if>
                    <xsl:call-template name="unescape">
                        <xsl:with-param name="escaped" select="$innercontent"/>
                    </xsl:call-template>
                </xsl:element>
                <xsl:call-template name="unescape">
                    <xsl:with-param name="escaped" select="$afterelem"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="unescapetext">
                    <xsl:with-param name="escapedtext" select="$escaped"/>
                </xsl:call-template>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <xsl:template name="unescapeattributes">
        <xsl:param name="escapedattributes"/>
        <xsl:variable name="attrname" select="substring-before($escapedattributes,'=')"/>
        <xsl:variable name="attrquote" select="substring($escapedattributes,string-length($attrname)+2,1)"/>
        <xsl:variable name="attrvalue" select="substring-before(substring-after($escapedattributes,$attrquote),$attrquote)"/>
        <xsl:variable name="afterattr" select="substring-after(substring-after($escapedattributes,$attrquote),$attrquote)"/>
        <xsl:attribute name="{$attrname}">
            <xsl:call-template name="unescapetext">
                <xsl:with-param name="escapedtext" select="$attrvalue"/>
            </xsl:call-template>
        </xsl:attribute>
        <xsl:if test="contains($afterattr,'=')">
            <xsl:call-template name="unescapeattributes">
                <xsl:with-param name="escapedattributes" select="normalize-space($afterattr)"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>

    <xsl:template name="unescapetext">
        <xsl:param name="escapedtext"/>
        <xsl:call-template name="string-replace-all">
            <xsl:with-param name="text">
                <xsl:call-template name="string-replace-all">
                    <xsl:with-param name="text">
                        <xsl:call-template name="string-replace-all">
                            <xsl:with-param name="text" select="$escapedtext"/>
                            <xsl:with-param name="replace">&amp;gt;</xsl:with-param>
                            <xsl:with-param name="by">&gt;</xsl:with-param>
                        </xsl:call-template>
                    </xsl:with-param>
                    <xsl:with-param name="replace">&amp;lt;</xsl:with-param>
                    <xsl:with-param name="by">&lt;</xsl:with-param>
                </xsl:call-template>
            </xsl:with-param>
            <xsl:with-param name="replace">&amp;amp;</xsl:with-param>
            <xsl:with-param name="by">&amp;</xsl:with-param>
        </xsl:call-template>
    </xsl:template>

    <!-- replaces substrings in strings -->
    <xsl:template name="string-replace-all">
        <xsl:param name="text"/>
        <xsl:param name="replace"/>
        <xsl:param name="by"/>
        <xsl:choose>
            <xsl:when test="contains($text, $replace)">
                <xsl:value-of select="substring-before($text,$replace)"/>
                <xsl:value-of select="$by"/>
                <xsl:call-template name="string-replace-all">
                    <xsl:with-param name="text" select="substring-after($text,$replace)"/>
                    <xsl:with-param name="replace" select="$replace"/>
                    <xsl:with-param name="by" select="$by"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$text"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- returns the substring after the last delimiter -->
    <xsl:template name="skipper-after">
        <xsl:param name="source"/>
        <xsl:param name="delimiter"/>
        <xsl:choose>
            <xsl:when test="contains($source,$delimiter)">
                <xsl:call-template name="skipper-after">
                    <xsl:with-param name="source" select="substring-after($source,$delimiter)"/>
                    <xsl:with-param name="delimiter" select="$delimiter"/>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$source"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

    <!-- returns the substring before the last delimiter -->
    <xsl:template name="skipper-before">
        <xsl:param name="source"/>
        <xsl:param name="delimiter"/>
        <xsl:param name="result"/>
        <xsl:choose>
            <xsl:when test="contains($source,$delimiter)">
                <xsl:call-template name="skipper-before">
                    <xsl:with-param name="source" select="substring-after($source,$delimiter)"/>
                    <xsl:with-param name="delimiter" select="$delimiter"/>
                    <xsl:with-param name="result">
                        <xsl:if test="result!=''">
                            <xsl:value-of select="concat($result,$delimiter)"/>
                        </xsl:if>
                        <xsl:value-of select="substring-before($source,$delimiter)"/>
                    </xsl:with-param>
                </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="$result"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>

</xsl:stylesheet>