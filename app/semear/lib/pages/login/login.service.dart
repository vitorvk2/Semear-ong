import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:semear/envs.dart';

Future makeLogin(BuildContext context) async {
  http.Response data = await http.post(
    Uri.parse(
      url_semear + "/api/login_aluno/",
    ),
    body: jsonEncode({"username": 'teste', "password": '13'}),
  );

  Map<String, dynamic> dataJson = jsonDecode(data.body);

  if (!dataJson['success']) {
    showDialog(
      context: context,
      builder: (c) {
        return AlertDialog(
          content: Text(dataJson['msg']),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: Text('Ok'),
            )
          ],
        );
      },
    );
  }
}
