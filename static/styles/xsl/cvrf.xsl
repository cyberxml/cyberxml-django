<?xml version="1.0" encoding="UTF-8"?>

<!--
    Document   : cvrf.xsl
    Created on : July 2, 2012, 9:58 AM
    Author     : chandan
    Description:
        Purpose of transformation follows.
	Original Source: http://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/1687073.xsl
-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
                xmlns:cvrf="http://www.icasi.org/CVRF/schema/cvrf/1.1"
                xmlns:vuln="http://www.icasi.org/CVRF/schema/vuln/1.1"
                xmlns:prod="http://www.icasi.org/CVRF/schema/prod/1.1"
                version="2.0"
                exclude-result-prefixes="cvrf"
                >
    <xsl:output method="html" standalone="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title><xsl:value-of select="//cvrf:DocumentTitle"/></title>
                <link type="text/css" rel="stylesheet" charset="UTF-8" href="1686935.css"/>
            </head>
            <body>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="cvrf:DocumentTitle">
        <h2 class="title"><span class="logo"></span><xsl:apply-templates/></h2>
    </xsl:template>

    <xsl:template match="cvrf:DocumentType|cvrf:Status|cvrf:Identification|cvrf:Version|cvrf:DocumentDistribution">
        <div><b><xsl:value-of select="local-name()"/>: </b> <xsl:apply-templates/></div>
    </xsl:template>
    <xsl:template match="cvrf:RevisionHistory|cvrf:DocumentReferences">
        <div><b><xsl:value-of select="local-name()"/></b><xsl:apply-templates/></div>
    </xsl:template>
    <xsl:template match="cvrf:DocumentTracking|cvrf:Revision|cvrf:Reference">
        <div>
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    <xsl:template match="cvrf:Note">
        <div>
            <xsl:apply-templates/>
        </div>
    </xsl:template>

    <xsl:template match="cvrf:InitialReleaseDate|cvrf:CurrentReleaseDate">
        <div><b><xsl:value-of select="local-name()"/>: </b>
            <xsl:call-template name="formatDate">
                <xsl:with-param name="dateTime" select="." />
        </xsl:call-template></div>
    </xsl:template>

    <xsl:template match="cvrf:Date">
        <xsl:call-template name="formatDate">
            <xsl:with-param name="dateTime" select="." />
        </xsl:call-template>
    </xsl:template>

    <xsl:template match="cvrf:Reference/cvrf:URL">
        <a><xsl:attribute name="href"><xsl:value-of select="."/></xsl:attribute>
            <xsl:value-of select="."/>
        </a>
    </xsl:template>

    <xsl:template match="cvrf:Acknowledgments">
        <div class="ack">
            <h2><span class="arrow"></span>Acknowledgments</h2>
            <dl>
                <xsl:apply-templates/>
            </dl>
        </div>
    </xsl:template>

    <xsl:template match="cvrf:Acknowledgment">
        <dd>
            <xsl:apply-templates/>
        </dd>
    </xsl:template>

    <xsl:template match="cvrf:Name">
        <b>
            <xsl:apply-templates/>
        </b>
    </xsl:template>
    <xsl:template match="prod:ProductTree">
        <div class="prod"><h2><span class="arrow"></span>Products Referenced</h2>
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    <xsl:template match="cvrf:Organization">
        - <xsl:apply-templates/>
    </xsl:template>

    <xsl:template match="prod:Branch[@Type='Product Version']" >
        <li>
            <xsl:apply-templates/>
        </li>
    </xsl:template>

    <xsl:template match="prod:Branch[@Type='Product Family']" >
        <b><xsl:value-of select="./@Type"/>: <xsl:value-of select="./@Name"/></b>
        <ul><xsl:apply-templates/>
        </ul>
    </xsl:template>

    <xsl:template match="prod:FullProductName" >
        <xsl:apply-templates/>
        (<xsl:value-of select="./@ProductID"/>)
    </xsl:template>

    <xsl:template match="vuln:Vulnerability" >
        <div class="vuln">
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    <xsl:template match="vuln:Title" >
        <h3>
            <span class="arrow"></span><xsl:apply-templates/>
        </h3>
    </xsl:template>
    <xsl:template match="vuln:Note" >
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    <xsl:template match="vuln:ReleaseDate">
        <b>Release Date: </b>
        <xsl:call-template name="formatDate">
            <xsl:with-param name="dateTime" select="." />
        </xsl:call-template>
    </xsl:template>
    <xsl:template match="vuln:CVE" >
        <div>
            <b>CVE id: </b>
            <a><xsl:attribute name="href">http://web.nvd.nist.gov/view/vuln/detail?vulnId=<xsl:value-of select="."/></xsl:attribute>
            <xsl:apply-templates/></a>
        </div>
    </xsl:template>

    <xsl:template match="vuln:Status" >
        <div>
            <b><xsl:value-of select="./@Type"/></b><dl>
            <xsl:apply-templates/></dl>
        </div>
    </xsl:template>
    <xsl:template match="vuln:ScoreSet" >
        <div>
            <b>CVSS Base Score <xsl:value-of select="vuln:BaseScore"/> </b>
            (<xsl:value-of select="./vuln:Vector"/>)
        </div>
        <div class="vector"><dl>
                <xsl:call-template name="printVector">
                    <xsl:with-param name="vec" select=
                                    "./vuln:Vector"/>
                </xsl:call-template>
        </dl></div>
    </xsl:template>

    <xsl:template match="vuln:ProductID" >
        <dd><xsl:value-of select="//prod:FullProductName[@ProductID=current()]"/>
            (<xsl:apply-templates/>)
        </dd>
    </xsl:template>
    <xsl:template match="vuln:Remediations" >
        <div><b>Remediation</b>
            <dl><xsl:apply-templates/></dl>
        </div>
    </xsl:template>

    <xsl:template match="vuln:Remediation" >
        <dd><b><xsl:value-of select="./@Type"/>: </b><a><xsl:attribute name="href"><xsl:value-of select="vuln:URL"/></xsl:attribute>
            <xsl:value-of select="vuln:Description"/></a>
        (<xsl:value-of select="vuln:Entitlement"/>)</dd>
        <xsl:apply-templates/>

    </xsl:template>
    <xsl:template match="vuln:Remediation/vuln:Entitlement|vuln:Remediation/vuln:URL|vuln:Remediation/vuln:Description" >
    </xsl:template>

    <xsl:template name="formatDate">
        <xsl:param name="dateTime" />
        <xsl:variable name="date" select="substring-before($dateTime, 'T')" />
        <xsl:variable name="year" select="substring-before($date, '-')" />
        <xsl:variable name="month" select="substring-before(substring-after($date, '-'), '-')" />
        <xsl:variable name="day" select="substring-after(substring-after($date, '-'), '-')" />
        <xsl:value-of select="concat($year, '-', $month, '-', $day)" />
    </xsl:template>

    <xsl:template name="printVector">
        <xsl:param name="vec" select="."/>
        <xsl:if test="string-length($vec)">
            <xsl:variable name="cv" select="substring-before(concat($vec,'/'),'/')"/>
            <xsl:variable name="c" select="substring-before($cv,':')"/>
            <xsl:variable name="v" select="substring-after($cv,':')"/>
            <xsl:variable name="C" select="Confidentiality"/>
            <xsl:variable name="I" select="Integrity"/>
            <xsl:variable name="A" select="Availability"/>
            <xsl:choose>
                <xsl:when test="$c = 'AV'">
                    <xsl:choose>
                        <xsl:when test="$v = 'N'"><dd class='AV R'><b>Access</b> Network</dd></xsl:when>
                        <xsl:when test="$v = 'A'"><dd class='AV O'><b>Access</b> Net Adj</dd></xsl:when>
                        <xsl:when test="$v = 'L'"><dd class='AV Y'><b>Access</b> Local</dd></xsl:when>
                    </xsl:choose>
                </xsl:when>
                <xsl:when test="$c = 'AC'">
                    <xsl:choose>
                        <xsl:when test="$v = 'L'"><dd class='AC R'><b>Complexity</b> Low</dd></xsl:when>
                        <xsl:when test="$v = 'M'"><dd class='AC O'><b>Complexity</b> Medium</dd></xsl:when>
                        <xsl:when test="$v = 'H'"><dd class='AC Y'><b>Complexity</b> High</dd></xsl:when>
                    </xsl:choose>
                </xsl:when>
                <xsl:when test="$c = 'Au'">
                    <xsl:choose>
                        <xsl:when test="$v = 'N'"><dd class='Au R'><b>Authentication</b> None</dd></xsl:when>
                        <xsl:when test="$v = 'S'"><dd class='Au O'><b>Authentication</b> Single</dd></xsl:when>
                        <xsl:when test="$v = 'M'"><dd class='Au Y'><b>Authentication</b> Multiple</dd></xsl:when>
                    </xsl:choose>
                </xsl:when>
                <xsl:when test="($c = 'A') or ($c = 'I') or ($c = 'C')">
                    <dd><xsl:attribute name="class"><xsl:value-of select="concat($v, ' I',$c)"/></xsl:attribute>
                        <b><xsl:choose>
                                <xsl:when test="$c = 'C'">Confidentiality </xsl:when>
                                <xsl:when test="$c = 'I'">Integrity </xsl:when>
                                <xsl:when test="$c = 'A'">Availability </xsl:when>
                            </xsl:choose>
                        </b>
                        <xsl:choose>
                            <xsl:when test="$v = 'C'">Complete</xsl:when>
                            <xsl:when test="$v = 'P'">Partial</xsl:when>
                            <xsl:when test="$v = 'N'">None</xsl:when>
                        </xsl:choose>
                    </dd>
                </xsl:when>
            </xsl:choose>
            <xsl:call-template name="printVector">
                <xsl:with-param name="vec" select=
                                "substring-after($vec,'/')"/>
            </xsl:call-template>
        </xsl:if>
    </xsl:template>

</xsl:stylesheet>
