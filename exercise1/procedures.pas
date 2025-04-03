Program procedures;

Procedure generateNumbers(Var data: Array Of Integer; first, last, size : Integer);

Var i, tmp : Integer;

Begin
  If size < 0 Then
    Begin
      writeln('ERROR: Number of elements to generate cannot be negative');
      exit;
    End;

  If first>last Then
    Begin
      tmp := last;
      last := first;
      first := tmp;
    End;

  For i := 0 To size-1 Do
    Begin
      data[i] := Random(last - first + 1) + first;
    End;
End;


Procedure print(Var data: Array Of Integer);

Var i: integer;

Begin
  For i := 0 To Length(data)-1 Do
    Begin
      Write(data[i], ' ');
    End;
  Writeln();
End;

Procedure sortArray(Var data: Array Of Integer);

Var i,j,tmp: integer;

Begin
  For i := 0 To Length(data)-2 Do
    For j := 0 To Length(data)-2 Do
      Begin
        If (data[j] > data[j+1]) Then
          Begin
            tmp := data[j];
            data[j] := data[j+1];
            data[j+1] := tmp;
          End;
      End;
End;







Var 
  dataArray: array Of integer;
  size: integer = 50;
Begin
  randomize;
  SetLength(dataArray, size);
  Writeln('Requirement for 3.0 and 4.0:');
  Writeln('Generated numbers:');
  generateNumbers(dataArray, 0, 100, size);
  print(dataArray);
  
  Writeln();

  Writeln('Requirement for 3.5:');
  writeln('Numbers after sorting:');
  sortArray(dataArray);
  print(dataArray);

End.