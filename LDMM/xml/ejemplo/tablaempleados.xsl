<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  
  <xsl:template match="//empresa">
    
    <table border="1">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Puesto</th>
          <th>email</th>
        </tr>
      </thead>
      <tbody>
        
        <xsl:for-each select="/empresa/departamentos/departamento/empleados/empleado">
          
          <tr>
            <td><xsl:value-of select="@id" /> </td>
            <td>
              <xsl:value-of select="nombre" />
            </td>
            <td>
              <xsl:value-of select="puesto" />
            </td>
            <td>
              <xsl:value-of select="email" />
            </td>
          </tr>
            
        </xsl:for-each>
      </tbody>

    </table>

  </xsl:template>
    
    
</xsl:stylesheet>
