import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:semear/envs.dart';
import 'package:shared_preferences/shared_preferences.dart';

Future<List<dynamic>> getFaltas(int id) async {
  SharedPreferences prefs = await SharedPreferences.getInstance();

  http.Response request = await http.get(
    Uri.parse(url_semear +
        '/api/chamada/aluno/' +
        id.toString() +
        '/' +
        (prefs.getInt('id_aluno') ?? 0).toString() +
        '/'),
    headers: {
      'Authorization': 'Bearer ' + (prefs.getString('token') ?? ''),
      'validate': 'Bearer ' + (prefs.getString('validate') ?? '')
    },
  );

  Map<String, dynamic> json = jsonDecode(request.body);

  return json['chamada_alunos'] as List<dynamic>;
}
