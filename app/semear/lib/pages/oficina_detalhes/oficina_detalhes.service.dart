import 'dart:convert';
import 'package:semear/envs.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

Future<Map<String, dynamic>> detalhesOficina(int id) async {
  SharedPreferences prefs = await SharedPreferences.getInstance();

  http.Response request = await http.get(
    Uri.parse(
        url_semear + '/api/oficinas/detalhealunos/' + id.toString() + '/'),
    headers: {
      'Authorization': 'Bearer ' + (prefs.getString('token') ?? ''),
      'validate': 'Bearer ' + (prefs.getString('validate') ?? '')
    },
  );

  Map<String, dynamic> dataJson = jsonDecode(request.body);

  return dataJson['oficina'] as Map<String, dynamic>;
}
