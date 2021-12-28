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

***

- Get Last Row
Gets last row given sheet & column passed in. Returns integer of row count

    Function getLastRow(sheet As String, Col As Variant) As Integer
        getLastRow = Sheets(sheet).Cells(Sheets(sheet).Rows.Count, Col).End(xlUp).Row
    End Function

***

- Clean Up Function
Basic clean up function for resetting workbook

    Function CleanUp()
        With Application
            .ScreenUpdating = True
            .DisplayAlerts = True
            .CutCopyMode = False
        End With
    End Function

***

- Hide Worksheets
Basic loop for hiding worksheets. `xlVeryHidden` sets worksheet not found even in right click. `xlHidden` or `.visible = False` hides worksheet from view

    Function HideSheets()
        With ActiveWorkbook
            .Sheets("SHEETNAME").Visible = xlVeryHidden
            .Sheets("SHEETNAME").Visible = xlHidden
        End With
    End Function

***

- Creating Pivot Table
Code for creating pivot table. Need to setup the `wb` var as ActiveWorkbook & `shName` as the sheet name. 

    Set tWs = wb.Sheets(shName)
    With tWs
        lRow = .Range("A2").End(xlDown).Row
        lCol = .Range("A2").End(xlToRight).Column
        srcData = .Name & "!" & .Range("A2", .Cells(lRow, lCol)).Address(ReferenceStyle:=xlR1C1)
    End With
    ' below code sets the name of the pivot table
    'pivotWs.Cells(6 + x - 4, 1).Value = tWs.Name & " Pivot Table"
    Set pCache = wb.PivotCaches.Create(SourceType:=xlDatabase, SourceData:=srcData)
    Set pTable = pCache.CreatePivotTable(TableDestination:=pivotWs.Cells(6 + x, 1), TableName:=shName)
    With pivotWs
        On Error Resume Next
        With pTable
            .ColumnGrand = True
            .HasAutoFormat = True
            .DisplayErrorString = False
            .DisplayNullString = True
            .EnableDrilldown = True
            .ErrorString = ""
            .MergeLabels = False
            .NullString = ""
            .PageFieldOrder = XlOrder.xlDownThenOver
            .PageFieldWrapCount = 0
            .PreserveFormatting = True
            .RowGrand = True
            .SaveData = True
            .PrintTitles = False
            .RepeatItemsOnEachPrintedPage = True
            .TotalsAnnotation = False
            .CompactRowIndent = 1
            .InGridDropZones = False
            .DisplayFieldCaptions = True
            .DisplayMemberPropertyTooltips = False
            .DisplayContextTooltips = True
            .ShowDrillIndicators = True
            .PrintDrillIndicators = False
            .AllowMultipleFilters = False
            .SortUsingCustomLists = True
            .FieldListSortAscending = False
            .ShowValuesRow = False
            .CalculatedMembersInFilters = False
            .RowAxisLayout xlCompactRow
            .RepeatAllLabels xlRepeatLabels
        End With
        With .PivotFields("Site")
            .Orientation = xlPageField
            .Position = 1
        End With
    End With