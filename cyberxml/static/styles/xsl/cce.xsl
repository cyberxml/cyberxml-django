<xsl:stylesheet xmlns="http://scap.nist.gov/schema/feed/configuration/0.1" xmlns:nvd="http://scap.nist.gov/schema/feed/configuration/0.1" xmlns:config="http://scap.nist.gov/schema/configuration/0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  xmlns:scap-core="http://scap.nist.gov/schema/scap-core/0.3" xsi:schemaLocation="http://scap.nist.gov/schema/configuration/0.1 http://nvd.nist.gov/schema/configuration_0.1.xsd http://scap.nist.gov/schema/scap-core/0.3 http://nvd.nist.gov/schema/scap-core_0.3.xsd http://scap.nist.gov/schema/feed/configuration/0.1 http://nvd.nist.gov/schema/nvd-cce-feed_0.1.xsd" version="1.0">
   <xsl:template match="/">
        <xsl:for-each select="//nvd:entry">
        <div>
            <h3>
                <xsl:value-of select="./config:cce-id"/><BR/>
            </h3><BR/>
        Summary: <xsl:value-of select="./config:summary"/><BR/>
        Published Date: <xsl:value-of select="./config:published-datetime"/><BR/>
        Last Modified: <xsl:value-of select="./config:last-modified-datetime"/><BR/>
                <xsl:value-of select="./config:cce-id"/><BR/>
        Scap Core Mappings:<BR/>
        <UL>
        <xsl:for-each select="//scap-core:mapping">
            <LI><xsl:value-of select="."/></LI>
        </xsl:for-each>
        </UL>
        </div>
        </xsl:for-each>
</xsl:template>
</xsl:stylesheet>