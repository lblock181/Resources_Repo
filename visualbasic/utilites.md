## VisualBasic Utility Functions

- Getting Column Number
Returns integer of column number if found, otherwise return -1
    
        Function GetColumnNumber(ws As Worksheet, colName As String, Optional rowOffset As Integer = 0, Optional fuzzySearch As Boolean = False) As Integer    
            For Each c In ws.Range(ws.Range("A1"), ws.Range("A1").offset(rowOffset, 0).End(xlToRight))
                Select Case fuzzySearch
                Case False
                    If c.Value = colName Then
                        GetColumnNumber = c.Column
                        Exit Function
                    End If
                Case True
                    If InStr(1, c.Value, colName, vbTextCompare) <> 0 Then
                        GetColumnNumber = c.Column
                        Exit Function
                    End If
                End Select
            Next c
            GetColumnNumber = -1
        End Function
