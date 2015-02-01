<xsl:stylesheet xmlns="http://scap.nist.gov/schema/feed/vulnerability/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:patch="http://scap.nist.gov/schema/patch/0.1" xmlns:vuln="http://scap.nist.gov/schema/vulnerability/0.4" xmlns:cpe-lang="http://cpe.mitre.org/language/2.0" xmlns:scap-core="http://scap.nist.gov/schema/scap-core/0.1" xmlns:cvss="http://scap.nist.gov/schema/cvss-v2/0.2" version="1.0">
    <xsl:template match="/">
    <div>
        <div>
            <h3>
                <xsl:value-of select="//vuln:cve-id"/>
            </h3>
        </div>
        <div>
            <xsl:value-of select="//vuln:summary"/>
        </div>
        <div>Published Date: <xsl:value-of select="//vuln:published-datetime"/>
        </div>
        <div>Last Modified: <xsl:value-of select="//vuln:last-modified-datetime"/>
        </div>
        <div>
            Security Protection: <xsl:value-of select="//vuln:security-protection"/>
        </div>
        <div>
            <strong>
                <u>Software List</u><br/>
            </strong>
        <ul>
            <xsl:for-each select="//vuln:product">
                <li>
                    <xsl:value-of select="."/>
                </li>
            </xsl:for-each>
        </ul>
        </div>
        <div>
            <strong>
                <u>Software Configuration</u><br/>
            </strong>
            <p>tbd</p>
        </div>
        <div>
            <strong>
                <u>CVSS Base Metrics</u>
            </strong>
        </div>
        <div>
        <br/>
        score: <xsl:value-of select="//cvss:score"/>
        <br/>
        access vector: <xsl:value-of select="//cvss:access-vector"/>
        <br/>
        access complexity: <xsl:value-of select="//cvss:access-complexity"/>
        <br/>
        authentication: <xsl:value-of select="//cvss:authentication"/>
        <br/>
        confidentiality impact: <xsl:value-of select="//cvss:confidentiality-impact"/>
        <br/>
        integrtity impact: <xsl:value-of select="//cvss:integrity-impact"/>
        <br/>
        availability impact: <xsl:value-of select="//cvss:availability-impact"/>
        <br/>
        source: <xsl:value-of select="//cvss:source"/>
        <br/>
        generated on: <xsl:value-of select="//cvss:generated-on-datetime"/>
        <br/>
        </div>
        <div>
        <strong>
            <u>References</u><br/>
        </strong>
        <xsl:for-each select="//vuln:references">
            <xsl:value-of select="vuln:source"/>: <xsl:value-of select="vuln:reference"/>
            <br/>
        </xsl:for-each>
        </div>
    </div>
    </xsl:template>
</xsl:stylesheet>