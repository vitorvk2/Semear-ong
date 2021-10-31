import 'package:flutter/material.dart';
import 'package:semear/pages/login/login.dart';
import 'package:semear/paletas/paleta.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Semear',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primarySwatch: SemearColor,
        ),
        home: LoginPage());
  }
}
