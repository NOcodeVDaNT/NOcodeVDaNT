<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>Student Information</title>
                <style>
                    table {
                        width: 50%;
                        border-collapse: collapse;
                        margin: 20px auto;
                    }
                    table, th, td {
                        border: 1px solid black;
                    }
                    th, td {
                        padding: 8px;
                        text-align: left;
                    }
                    th {
                        background-color: #6a5acd;
                        color: white;
                    }
                </style>
            </head>
            <body>
                <h2 style="text-align: center;">Student Information</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Enrollment</th>
                            <th>Name</th>
                            <th>Mobile Number</th>
                            <th>Email ID</th>
                        </tr>
                    </thead>
                    <tbody>
                        <xsl:for-each select="students/student">
                            <tr>
                                <td><xsl:value-of select="enrollment" />0701cs231064</td>
                                <td><xsl:value-of select="name" />ghost</td>
                                <td><xsl:value-of select="mobile" />9539475xxx</td>
                                <td><xsl:value-of select="email" />ujegfxxx@gmail.com</td>
                            </tr>
                        </xsl:for-each>
                    </tbody>
                </table>
            </body>
        </html>
    </xsl:template>
    
</xsl:stylesheet>