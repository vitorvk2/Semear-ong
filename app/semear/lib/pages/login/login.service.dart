import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:semear/envs.dart';
import 'package:semear/pages/home/home.dart';
import 'package:shared_preferences/shared_preferences.dart';

final TextEditingController user_ctrl = TextEditingController();
final TextEditingController password_ctrl = TextEditingController();

Future<bool> makeLogin(BuildContext context) async {
  http.Response data = await http.post(
    Uri.parse(
      url_semear + "/api/login_aluno/",
    ),
    body: jsonEncode({
      "username": user_ctrl.text,
      "password": password_ctrl.text,
    }),
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

    return false;
  }

  SharedPreferences prefs = await SharedPreferences.getInstance();

  prefs.setInt('id_aluno', dataJson['data']['id']);
  prefs.setString('token', dataJson['token']);
  prefs.setString('validate', dataJson['validate']);

  return true;
}

Future checkLogin(BuildContext ctx) async {
  SharedPreferences prefs = await SharedPreferences.getInstance();

  if ((prefs.getString('token') ?? '') != '') {
    http.Response data = await http.post(
      Uri.parse(
        url_semear + "/api/validate/",
      ),
      headers: {
        'Authorization': 'Bearer ' + (prefs.getString('token') ?? ''),
        'validate': 'Bearer ' + (prefs.getString('validate') ?? '')
      },
    );

    if (data.statusCode != 200) {
      prefs.clear();
      return;
    }

    Navigator.of(ctx).pushAndRemoveUntil(
      CupertinoPageRoute(builder: (ctx2) => HomePage()),
      (router) => false,
    );
  }
}
